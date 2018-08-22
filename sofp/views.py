from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello Stackoverflow's tags Predictor")
    return render(request, 'home.html')
