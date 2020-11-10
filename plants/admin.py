from django.contrib import admin

# Register your models here.
from .models import Plant, Watering
admin.site.register(Plant)
admin.site.register(Watering)
