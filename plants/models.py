from django.db import models
from django.urls import reverse
# Create your models here.

FERTILIZERS =(
  ('O', 'Once a Month'),
  ('T', 'Twice a Month')
)
WATERS =(
  ('O', 'Once a Week'),
  ('T', 'Twice a Week')
) 
class Accessory(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})

class Plant(models.Model):
  name = models.CharField(max_length=100)
  care_level = models.CharField(max_length=100)
  description = models.TextField()
  age = models.IntegerField()
  accessories = models.ManyToManyField(Accessory)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'plant_id':self.id})

class Watering(models.Model):
  date = models.DateField('Watering Date')
  fertilizer = models.CharField(
    max_length=1,
    choices = FERTILIZERS,
    default = FERTILIZERS[0][0]
  )
  water = models.CharField(
    max_length=1,
    choices=WATERS,
    default = WATERS[0][0]
  )
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_fertilizer_display()} and {self.get_water_display()} on {self.date}"


