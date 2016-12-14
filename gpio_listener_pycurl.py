#!/usr/bin/python

# ------ IMPORTS -----

import os
import time
# import RPi.GPIO as GPIO # use when deployed in raspi
import test_rpi_gpio as GPIO
# import pycurl
from io import BytesIO
import time

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode


# ----- CONFIGURATIONS -----

SLAVE_ID = 1  # This should be unique for every slave (i.e. )
MASTER_ADDRESS = '127.0.0.1/notification'
CURL_TIMEOUT = 2 
RETRY_COUNT = 3

class GPIOListener(object):
    """
        A GPIO listener slave that notifies its 
        master when the physical button was pushed  
        
        :author: Jhesed Tacadena
        :date: 2016-04-22

        TODO: logging to text file/DB/redis
    """

    def __init__(self, refresh_sec=1, curl_timeout=2):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(10, GPIO.IN)
        self.refresh_sec = refresh_sec
        self.curl_timeout = curl_timeout


    def listen(self):
        """
            Waits for physical button to be pressed and
            send signal to master when this happens
        """

        print('Initial Switch Status: ', GPIO.input(10))

        while True:
            if GPIO.input(10) == False:  # button was pressed
                print("Button Pressed, Notifying master")
                os.system('date')
                print(GPIO.input(10))
                response = self.notify_master()
                print(response)
                time.sleep(5)
            else:
                os.system('clear')
                print ("Waiting for you to press a button")
        
            time.sleep(self.refresh_sec)


    def notify_master(self, decoding='iso-8859-1', timeout=3):
        """
            Notifies signal to master
            Options:
                (1) Drop via redis (retrievable via brpop)
                (2) Text file
                (3) Curl (simplest, but dangerous when master is dead)
                (4) ZMQ -- tideous, overkill
        """

        # let's use the simplest solution for now

        # our post fields
        post_data = {'id': SLAVE_ID}  # TODO: add encryption
        postfields = urlencode(post_data)

        # setup pycurl
        # buffer = BytesIO()

        # # pycurl version
        # c = pycurl.Curl()
        # c.setopt(c.URL, MASTER_ADDRESS)
        # c.setopt(c.WRITEDATA, buffer)
        # c.setopt(c.VERBOSE, True)
        # c.setopt(c.VERBOSE, TIMEOUT, timeout)
        # c.setopt(c.POSTFIELDS, postfields)

        retries = 0 
        response = 'Empty Response'

        while retries < RETRY_COUNT:
            try:


                # ----- urllib version -----
                response = urllib.urlopen(MASTER_ADDRESS, params)
                if response:
                    print(response.read())
                    retries = 0
                else:
                    time.sleep(1)

                # ----- pycurl version -----

                # # hit master url
                # c.perform()

                # response = buffer.getvalue()
                # # response is a byte string.
                # # We have to know the encoding in order 
                # # to print it to a text file
                # # such as standard output.
                # print(response.decode(decoding))

                # reset retry counter
                break # exit loop. no retry needed
            # except (pycurl.error, error):
            except error:
                errno, errstr = error
                print('An error occurred: ', errstr)
                retries += 1 
            # finally:
                # pycurl version
                # c.close()


        return response


if __name__ == 'main':
    slave_obj = GPIOListener()
    slave_obj.listen()