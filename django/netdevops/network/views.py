from django.shortcuts import render
from django.http import HttpResponse
import logging
import sys

"""
logging.basicConfig(level=logging.INFO) # Here
logging.debug("Log message goes here.")
logging.info("Log message goes here.")
logging.warning("Log message goes here.")
logging.error("Log message goes here.")
logging.critical("Log message goes here.")
"""
logger = logging.getLogger('django')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# Create your views here.
def monthly(request, month):
    # for loop over months checling months
    for i in months:
        if month.lower() == i.lower():
            return HttpResponse(f"{i}")

def monthlyNumbers(request, month):
    for i in range(len(months)):
        if int(month) == i+1:
            return HttpResponse(f"{month}")