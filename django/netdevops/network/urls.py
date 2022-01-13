from django.urls import path
from . import views

# sub pages under the network section below is an example of webpage/network/commands page referencing the index function
urlpatterns = [
    path("index", views.index, name="index"),
    path("commands", views.commands, name="commands"),
    path("january", views.january, name="january")
]