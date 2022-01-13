from django.urls import path
from . import views

urlpatterns = [
    path("commands", views.index, name="index")
]