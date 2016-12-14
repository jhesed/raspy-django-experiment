from django.shortcuts import render
from notification.models import Notification
from villager.models import Villager

# from django.http import HttpResponse


def index(request):
    """
    Renders the map and plot all markers where
    GPIO events are active
    """

    # lets get all active notifications
    # this will return a Django query set object
    # .values() convert it to list of dictionaies
    notifs = Notification.objects.filter(is_active=1).values()
    villagers = []

    # let's extract coordinates here because django 
    # templates does not allow logic there

    coords = {}
    for i, notif in enumerate(notifs):
        coords_xyz = notif['house_coordinates'].split(',')
        print(notifs[i])
        notifs[i]['coords_left'] = coords_xyz[0]
        notifs[i]['coords_top'] = coords_xyz[1]
        
        villagers.append(Villager.objects.get(pk=notif['villager_id']))
        
    return render(request, 'village/index.html', 
        {'notif_villagers': zip(notifs, villagers) })
        # {'notifs': notifs, 'villagers': villagers})