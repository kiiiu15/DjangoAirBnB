from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from datetime import datetime


def index(request):
    return render(request, "Airbnb/welcome.html")


@csrf_exempt
def showAvailable(request):
    print(request.POST)

    fromDate = request.POST['dateFrom']
    toDate = request.POST['dateTo']

    # fromDate = "2020-10-22"
    # toDate = "2020-10-23"
    date_format = "%Y-%m-%d"
    a = datetime.strptime(fromDate, date_format)
    b = datetime.strptime(toDate, date_format)

    days = (b - a).days + 1
    print(days)
    properties = []

    for property in models.Property.objects.all():
        if property.dates.filter(date__range=[fromDate, toDate], reservation=None).count() == days:
            properties.append(property)

    print(properties)
    # return HttpResponse("<p>No jodas.. </p>")
    return render(request, "Airbnb/index2.html", {"properties": properties, "from": fromDate, "to": toDate})




class ShowProperty(generic.DetailView):
    model = models.Property
    template_name_suffix = ""
    template_name = "Airbnb/"