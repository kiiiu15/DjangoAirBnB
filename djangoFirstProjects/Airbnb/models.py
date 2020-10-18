from django.db import models


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, default="No name provided")

    def __str__(self):
        return "This is the city: " + self.name
