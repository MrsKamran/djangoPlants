from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Plant


num = 5

def home(request):
    return HttpResponse("Hello, You're at the plants home.")

def about(request):
    return render(request, 'about.html',{'num': num})

def plants_index(request):
    plants=Plant.objects.all()
    return render(request, 'plants/index.html', {'plants':plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', {'plant':plant})



