from django.shortcuts import render, redirect
import json
from .forms import *


# Create your views here.
def home(request):
    # example
    events = [
        {"id": 'a', "title": 'my event', "start": "2022-01-06", "end": "2022-01-08",
         "description": 'This is a cool event'},
        {"id": 'b', "title": 'my event 2', "start": "2022-01-08", "description": 'This is a cool event 2'}]
    if not request.user.is_authenticated:
        return redirect('Auth:login')
    return render(request, 'home.html', {"user": request.user, "events": json.dumps(events)})


def front(request):
    return render(request, 'front.html', {"user": request.user})


def new_medication(request):
    if not request.user.is_authenticated:
        return redirect('Auth:login')

    if request.method != 'POST':
        form = MedicationForm()

    else:
        form = MedicationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('MedicationScheduler:home')

    context = {'form': form}
    return render(request, 'new_medication.html', context)


def new_prescription(request):
    # only logged in users can add a prescription
    if not request.user.is_authenticated:
        return redirect('Auth:login')

    if request.method != 'POST':
        form = PrescriptionForm()

    else:
        form = PrescriptionForm(data=request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.user = request.user
            prescription.save()
            return redirect('MedicationScheduler:home')

    context = {'form': form}
    return render(request, 'new_prescription.html', context)
