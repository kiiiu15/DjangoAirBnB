from django.urls import path
from . import views

app_name = "Airbnb"
urlpatterns = [
    path("", views.CityList.as_view(), name="List"),
    path("<int:pk>", views.CityDetail.as_view(), name="Detail"),
    path("Add/", views.CityAdd.as_view(), name="Add"),
    path("<int:pk>/Update", views.CityUpdate.as_view(), name="Update"),
    path("<int:pk>/Delete", views.CityDelete.as_view(), name="Delete"),

]
