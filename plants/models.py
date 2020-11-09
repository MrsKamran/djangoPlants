from django.db import models

# Create your models here.

class Plant(models.Model):
  name = models.CharField(max_length=100)
  care_level = models.CharField(max_length=100)
  description = models.TextField()
  age = models.IntegerField()

  def __str__(self):
    return self.name