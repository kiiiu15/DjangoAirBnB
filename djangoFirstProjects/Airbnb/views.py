from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from . import models


# Create your views here.
class CityList(generic.ListView):
    model = models.City
    context_object_name = "cityList"
    template_name = "Airbnb/ListView.html"

    def get_queryset(self):
        return models.City.objects.all()


class CityDetail(generic.DetailView):
    model = models.City
    template_name = "Airbnb/DetailView.html"


class CityAdd(generic.CreateView):
    template_name_suffix = ""
    fields = ["name"]
    model = models.City
    template_name = "Airbnb/AddView.html"
    success_url = "/City/"


class CityUpdate(generic.UpdateView):
    template_name_suffix = ""
    fields = ["name"]
    model = models.City
    template_name = "Airbnb/UpdateView.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return "/City/%i" % pk


class CityDelete(generic.DeleteView):
    model = models.City
    template_name_suffix = ""
    template_name = "Airbnb/DeleteView.html"
    success_url = "/City/"
