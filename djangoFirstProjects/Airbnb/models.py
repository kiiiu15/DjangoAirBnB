from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, default="No name provided")

    def __str__(self):
        return "This is the city: " + self.name


class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    tittle = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    pricePerDay = models.FloatField(default=0.0)
    maxPeople = models.IntegerField()
    photo = models.ImageField()

    def __str__(self):
        return self.tittle


