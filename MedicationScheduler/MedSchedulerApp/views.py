from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html', {"user": request.user})

def new_medication(request):
    print("form reached")
    if request.method != 'POST':
        print("empty form")
        form = MedicationForm()
    
    else:
        print("prepping to submit")
        form = MedicationForm(data=request.POST)
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
        
