from django.shortcuts import render
from django.http import HttpResponse
import logging

"""
logging.basicConfig(level=logging.INFO) # Here
logging.debug("Log message goes here.")
logging.info("Log message goes here.")
logging.warning("Log message goes here.")
logging.error("Log message goes here.")
logging.critical("Log message goes here.")
"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# Create your views here.
def monthly(request, month):
    # for loop over months checling months
    for i in months:
        if month.lower() == i.lower():
            return HttpResponse(f"{i}")

def monthlyNumbers(request, month):
    print(f"incoming month: {month}"+ " type: "+ str(type(month)))
    for i in range(len(months)):
        if month == i+1:
            return HttpResponse(f"{months[i]}")