from django.urls import path
from . import views

urlpatterns = [
    path("/network/", views.index, name="index")
]