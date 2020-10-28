from django.urls import path
from . import views

app_name = "Airbnb"
urlpatterns = [

     path("", views.index, name="Index"),
     path("asd", views.showAvailable, name="List"),
    # path("", views.CityList.as_view(), name="List"),
    # path("<int:pk>", views.CityDetail.as_view(), name="Detail"),

]
