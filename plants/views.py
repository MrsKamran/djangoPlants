from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Plant:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, care_level, description, age):
    self.name = name
    self.care_level = care_level
    self.description = description
    self.age = age

plants = [
  Plant('Snake Plant', 'Basic', 'Bush', 2),
  Plant('Spider Plant', 'Basic', 'Bush',0),
  Plant('Pothos', 'Medium', 'Vine', 4),
  Plant('Aloe Vera', 'Basic', 'Bush', 3),
  Plant('Broad Leaf Oregano', 'Medium', 'Vine', 4),
  Plant('English Ivy', 'Medium', 'Vine', 3),
  Plant('Broad leaf Lemon Thyme', 'Basic', 'Bush', 3),
]


def home(request):
    return HttpResponse("Hello, You're at the plants home.")

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {'plants':plants})

