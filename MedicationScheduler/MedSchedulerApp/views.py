from django.shortcuts import render, redirect
from .forms import *


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user})
    else:
        return redirect('login')
    

def new_medication(request):
    if request.method != 'POST':
        print("empty form")
        form = MedicationForm()
    
    else:
        
        form = MedicationForm(data=request.POST)
        print("prepping to submit", form.is_valid())
        print(form.errors)
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect('MedicationScheduler:home')
    
    context = {'form': form}
    return render(request, 'new_medication.html', context)


def new_prescription(request):
    print("form reached")
    if request.method != 'POST':
        print("empty form")
        form = PrescriptionForm()
    
    else:
        form = PrescriptionForm(data=request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect('MedicationScheduler:home')
    
    context = {'form': form}
    return render(request, 'new_prescription.html', context)
