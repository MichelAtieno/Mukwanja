from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render,redirect
from .models import Event

# Create your views here.
def welcome(request):
    events = Event.get_events()
    return render(request, 'home.html', {'events':events})

def single_event(request,event_id):
    event = Event.get_event(event_id)

    return render(request,"event.html", {'event':event})