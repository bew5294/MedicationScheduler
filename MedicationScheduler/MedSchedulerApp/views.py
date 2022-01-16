import json
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import *
from multi_form_view import MultiModelFormView
from datetime import datetime, date
from datetime import timedelta


# Create your views here.
def home(request):
    # example
    # events = [
    #     {"id": 'a', "title": 'my event', "start": "2022-01-06", "end": "2022-01-08",
    #      "description": 'This is a cool event'},
    #     {"id": 'b', "title": 'my event 2', "start": "2022-01-08", "description": 'This is a cool event 2'}]
    
    events = getEvents(request.user)
    if not request.user.is_authenticated:
        return redirect('Auth:login')
    return render(request, 'home.html', {"user": request.user, "events": json.dumps(events, default=str)})


def getEvents(user):
    schedule = Schedule.objects.get(user=user)
    elements = ScheduleElement.objects.filter(schedule=schedule)
    
    events = []
    
    # daysOfWeek
    # startTime
    # endTime
    # startRecur
    # endRecur
    # groupId
    
    for element in elements:
        weekdays = []
        if element.sunday:
            weekdays.append(0)
        if element.monday:
            weekdays.append(1)
        if element.tuesday:
            weekdays.append(2)
        if element.wednesday:
            weekdays.append(3)
        if element.thursday:
            weekdays.append(4)
        if element.friday:
            weekdays.append(5)
        if element.saturday:
            weekdays.append(6)
        
        events.append(
            {
                'id':         element.id,
                'title':      element.prescription.medication.name,
                'startTime':  element.time,
                # 'endTime':    element.time + timedelta(minutes=15),
                # 'endTime':    element.time + datetime.time(15,0),
                'startRecur': date.today(),
                'endRecur':   element.prescription.discard_after,
                'daysOfWeek': weekdays
            }
        )
    
    return events


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
    if not request.user.is_authenticated:
        return redirect('Auth:login')

    if request.method != 'POST':
        presc_form = PrescriptionForm()
        sched_form = ScheduleElementForm()

    else:
        # if the toggle button is clicked attempt to submit both forms
        if request.POST.get("toggle-btn"):
            presc_form = PrescriptionForm(data=request.POST)
            sched_form = ScheduleElementForm(data=request.POST)

            if presc_form.is_valid() and sched_form.is_valid():
                prescription = presc_form.save(commit=False)
                prescription.user = request.user
                prescription.save()

                schedule_element = sched_form.save(commit=False)
                schedule_element.schedule = Schedule.objects.get(
                    user=request.user)
                schedule_element.prescription = prescription
                schedule_element.save()

                return redirect('MedicationScheduler:home')

        # if not only attempt to submit prescription form
        else:
            form = PrescriptionForm(data=request.POST)
            if form.is_valid():
                prescription = form.save(commit=False)
                prescription.user = request.user
                prescription.save()
                return redirect('MedicationScheduler:home')

    context = {'presc_form': presc_form, 'sched_form': sched_form}
    return render(request, 'new_prescription.html', context)
