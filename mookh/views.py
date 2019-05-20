from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render,redirect

# Create your views here.
def welcome(request):
    return render(request, 'home.html')