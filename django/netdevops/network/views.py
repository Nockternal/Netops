from django.shortcuts import render
from django.http import HttpResponse
import logging
import sys

monthly_challenges = {
    'January': 'challenge-1',
    'February': 'challenge-2',
    'March': 'challenge-3',
    'April': 'challenge-4',
    'May': 'challenge-5',
    'June': 'challenge-6',
    'July': 'challenge-7',
    'August': 'challenge-8',
    'September': 'challenge-9',
    'October': 'challenge-10',
    'November': 'challenge-11',
    'December': 'challenge-12'
}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# Create your views here.
def monthly(request, month):
    # for loop over months checling months
    try:
        monthly_challenges[month]
    except:
        for i in months:
            if month.lower() == i.lower():
                return HttpResponse(f"{i}")

def monthlyNumbers(request, month):
    for i in range(len(months)):
        if int(month) == i+1:
            return HttpResponse(f"{month}")