from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.models import User
import datetime as dt
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Event

# Create your views here.
def welcome(request):
    events = Event.get_events()
    return render(request, 'home.html', {'events':events})

def single_event(request,event_id):
    event = Event.get_event(event_id)
    if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                redirect('login.html')
    else:
        form=RegistrationForm()

    return render(request,"event.html", {'event':event, 'form':form})

def register(request):
    if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                redirect('login.html')
    else:
        form=RegistrationForm()
        return render(request, 'registration/registration_form.html', {'form':form})


