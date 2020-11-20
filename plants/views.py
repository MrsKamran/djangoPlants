from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .models import Plant, Accessory
from .forms import WateringForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

num = 5

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['name', 'care_level', 'description', 'age']
    def form_valid(self, form):
      form.instance.user = self.request.user  
      return super().form_valid(form)

class PlantUpdate(UpdateView):
    model = Plant
    fields = "__all__"

class PlantDelete(DeleteView):
    model = Plant
    success_url = "/plants/"


def home(request):
    # return HttpResponse("Hello, You're at the plants home.")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html',{'num': num})

@login_required
def plants_index(request):
    # plants=Plant.objects.all()
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', {'plants':plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    accessories_plant_doesnt_have = Accessory.objects.exclude(id__in = plant.accessories.all().values_list('id'))
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {'plant':plant, 'watering_form':watering_form, 'accessories':accessories_plant_doesnt_have})

def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

def assoc_accessory(request, plant_id, accessory_id):
  # Note that you can pass a toy's id instead of the whole object
  Plant.objects.get(id=plant_id).accessories.add(accessory_id)
  return redirect('detail', plant_id=plant_id)

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/toys/'