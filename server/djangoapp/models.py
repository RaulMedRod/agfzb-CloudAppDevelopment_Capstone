from django.db import models
from django.utils.timezone import now


# Create your models here.

from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dealer_id = models.IntegerField() 
    TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add other choices as needed
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.DateField()

    def __str__(self):
        return f"{self.car_make.name} - {self.name}"



# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
