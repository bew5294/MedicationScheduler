from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('Auth:login')
    return render(request, 'home.html', {"user": request.user})


def front(request):
    return render(request, 'front.html', {"user": request.user})
    

def new_medication(request):
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
    if request.user.is_authenticated:
        print("form reached")
        if request.method != 'POST':
            print("empty form")
            form = PrescriptionForm()
        
        else:
            form = PrescriptionForm(data=request.POST)
            if form.is_valid():
                print("form is valid")
                prescription = form.save(commit=False)
                prescription.account = request.user
                prescription.save()
                return redirect('MedicationScheduler:home')
        
        context = {'form': form}
        return render(request, 'new_prescription.html', context)
    else:
        return redirect('login')
