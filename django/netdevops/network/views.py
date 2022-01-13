from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('This is up')
    #return render(request, 'network/pages/index.html')
    
def commands(request):
    return HttpResponse('commands')
    #return render(request, 'network/pages/commands.html')

def january(request):
    return HttpResponse('january')