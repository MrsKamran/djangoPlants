from django.contrib import admin

# Register your models here.
from .models import Plant, Watering, Accessory
admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Accessory)
