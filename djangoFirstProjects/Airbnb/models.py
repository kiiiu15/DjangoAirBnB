from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import admin
from django.utils import timezone


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
    photo = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.tittle


class Reservation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    date = models.DateField(default=timezone.now())
    code = models.CharField(max_length=70, default=str(timezone.now()))
    subtotal = models.FloatField(default=0.0)
    commission = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)
    guestName = models.CharField(max_length=50)
    guestLastName = models.CharField(max_length=50)
    guestEmail = models.EmailField()

    def __str__(self):
        return self.code


class DateRental(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="dates")
    reservation = models.ForeignKey(Reservation, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class DateRentalInline(admin.TabularInline):
    model = DateRental
    fk_name = "property"
    max_num = 7


class PropertyAdmin(admin.ModelAdmin):
    inlines = [DateRentalInline, ]
