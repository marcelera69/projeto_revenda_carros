from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year= models.IntegerField()
    model_year= models.IntegerField()
    km = models.IntegerField()
    value= models.FloatField()
    photo = models.ImageField(upload_to='cars/')
    description = models.TextField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.model
    

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}  at:{self.created_At}'