from django.shortcuts import render
from django.http import HttpResponse

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# Create your views here.
def monthly(request, month):
    # for lopp over months checling months
    for i in months:
        if month.lower() == i:
            return HttpResponse(f"{month}")
        elif month == i:
            return HttpResponse(f"{month}")

