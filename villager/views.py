from django.shortcuts import render
from villager.models import Villager

# Create your views here.

# def add(request):
# 	context = {}
# 	return render(request, 'villager/add.html', context)

def get(request):
    _id = request.GET.get('j')
    vill = Villager.objects.get(pk=_id)
    return render(request, 'villager/info.html', {'villager': vill})   