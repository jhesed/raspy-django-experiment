#!/usr/bin/env python
#
# Runs a Tornado web server with a django project
# Make sure to edit the DJANGO_SETTINGS_MODULE to point to your settings.py
#
# http://localhost:8080/hello-tornado
# http://localhost:8080

import sys
import os

from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
from tornado import websocket
from django.core.wsgi import get_wsgi_application
import json
import logging

GLOBALS={
    'sockets': []
}

logger = logging.getLogger(__name__)

define('port', type=int, default=8888)

class ClientSocket(websocket.WebSocketHandler):
    def open(self):
        GLOBALS['sockets'].append(self)
        print("WebSocket opened")

    def on_close(self):
        print("WebSocket closed")
        GLOBALS['sockets'].remove(self)


class CometServer(tornado.web.RequestHandler):
    """
    Acts as a comet server that notifies javascript
    to update real time
    """
    def get(self, *args, **kwargs):

        # ----- local imports -----

        from villager.models import Villager
        from notification.models import Notification

        _id = self.get_argument('id')
        vill = Villager.objects.get(pk=_id)

        notif = Notification.objects.filter(villager_id=_id, is_active=1)
        if not notif:
            # let us save this as new notification for logging purpose and so that
            # we can use it later
            notif = Notification(villager_id=_id, house_coordinates=vill.house_coordinates,
                gmap_coordinates=vill.gmap_coordinates, is_active=1)
            notif.save()

            # we need to convert this to js readable format
            data = {
                'id': vill.id,
                'first_name': vill.first_name,
                'middle_name': vill.middle_name,
                'last_name': vill.last_name,
                'phone_number': vill.phone_number,
                'lot_number': vill.lot_number,
                'house_coordinates': vill.house_coordinates,
                'gmap_coordinates': vill.gmap_coordinates,
            }

            for socket in GLOBALS['sockets']:
                socket.write_message(json.dumps(data))
            logger.info(data)
            self.write('Notified')
        else:
            self.write('Alarm already active')

        return

    def post(self, *args, **kwargs):
        """
        Used to update a notification object.
        Example: 
            - Disabling the alarm
        """
        
        # ----- local imports -----

        from villager.models import Villager
        from notification.models import Notification
        

        _id = self.get_argument('id')
        
        try:
            _id = int(_id)
            notif = Notification.objects.get(pk=_id)
            
            # let's disable the alarm
            notif.is_active = 0
            notif.save()
            self.write('Deactivated')
        except ValueError:
            logger.error('Invalid ID')
            self.write('Invalid ID')

        return

def main():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }
    os.environ['DJANGO_SETTINGS_MODULE'] = 'village_security.settings' # TODO: edit this
    sys.path.append('static') # path to your project if needed
  
    parse_command_line()

    wsgi_app = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(wsgi_app)

    tornado_app = tornado.web.Application(
        [
            (r'/static/(.*)', tornado.web.StaticFileHandler, 
                {'path': "{0}/static".format(os.getcwd())}),
            (r"/socket", ClientSocket),
            (r"/notification", CometServer),
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ])

    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()