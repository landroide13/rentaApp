from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email    = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=30, blank=False)



class Car(models.Model):
    brand = models.CharField(max_length=150, blank=False)
    model = models.CharField(max_length=200, blank=False)
    color = models.CharField(max_length=30, blank=False)
    plate = models.IntegerField(blank=False)
    image = models.ImageField(upload_to="cars_img/", height_field=None, width_field=None)



    
