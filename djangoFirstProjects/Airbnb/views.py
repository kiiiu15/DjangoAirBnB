from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from . import models


def index(request):
    return HttpResponse("<H1>Hello world 1</H1>")
