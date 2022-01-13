from django.urls import path
from . import views

# sub pages under the network section below is an example of webpage/network/commands page referencing the index function
urlpatterns = [
    path("<str:month>", views.monthly, name="monthly"),
    path("<int:month>", views.monthlyNumbers, name="monthly"),
]