from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from . import models


def index(request):
    return render(request, "Airbnb/welcome.html", {"cities": models.City.objects.all()})


@csrf_exempt
def showAvailable(request):
    fromDate = request.POST['dateFrom']
    toDate = request.POST['dateTo']
    date_format = "%Y-%m-%d"
    a = datetime.strptime(fromDate, date_format)
    b = datetime.strptime(toDate, date_format)

    days = (b - a).days + 1
    properties = []

    maxPax = request.POST["maxPax"]
    city = request.POST["city"]

    for property in models.Property.objects.filter(maxPeople__gte=maxPax, city__id=city):
        if property.dates.filter(date__range=[fromDate, toDate], reservation=None).count() == days:
            properties.append(property)

    return render(request, "Airbnb/index2.html",
                  {"properties": properties, "from": fromDate, "to": toDate, "max": maxPax,
                   "cities": models.City.objects.all().exclude(pk=city), "selected": models.City.objects.get(pk=city)})


def ShowProperty(request, pk):
    fromDate = request.POST['dateFrom']
    toDate = request.POST['dateTo']
    date_format = "%Y-%m-%d"
    a = datetime.strptime(fromDate, date_format)
    b = datetime.strptime(toDate, date_format)

    days = (b - a).days + 1
    obj = get_object_or_404(models.Property, pk=pk)

    subtotal = days * obj.pricePerDay
    comision = subtotal * 0.08
    total = subtotal + comision

    return render(request, "Airbnb/detail.html",
                  {"object": obj, "from": fromDate, "to": toDate, "idProperty": pk, "subtotal": subtotal,
                   "comision": comision, "total": total})


def ReserveProperty(request, idProperty):
    print(request.POST)
    data = request.POST
    property = models.Property.objects.get(pk=idProperty)
    reservation = models.Reservation(property=property, subtotal=data['subtotal'], commission=data['comission'],
                                     total=data['total'], guestName=data['guestName'],
                                     guestLastName=data['guestLastName'], guestEmail=data['guestEmail'])

    reservation.save()

    datesSelected = property.dates.filter(date__range=[data['dateFrom'], data['dateTo']], reservation=None)

    for date in datesSelected:
        date.reservation = reservation
        date.save()

    return render(request, "Airbnb/welcome.html", {"cities": models.City.objects.all(), "message" : "Thank you for your reservation!"})

