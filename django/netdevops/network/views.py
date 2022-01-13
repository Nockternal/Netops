from django.shortcuts import render
from django.http import HttpResponse

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# Create your views here.
def monthly(request, month):
    # for loop over months checling months
    for i in months:
        if month.lower() == i.lower():
            return HttpResponse(f"{i}")

def monthlyNumbers(request, month):
    for i in range(len(months)):
        if month == i+1:
            return HttpResponse(f"{months[i]}")