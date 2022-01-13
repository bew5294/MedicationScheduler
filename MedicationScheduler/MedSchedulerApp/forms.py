from django import forms
from django.forms import widgets, DateField
from django.db.models import fields
from MedSchedulerApp.models import *


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = [
            'name',
            'ndc',
            'dose',
            'strength'
        ]
    

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Presciption
        fields = [
            'medication',
            'directions',
            'quantity',
            'refills',
            'prescriber',
            'scanned_label',
            'date_filled',
            'discard_after'
        ]
        
        widgets = {
            'date_filled': widgets.DateInput(attrs={'type': 'date'}),
            'discard_after': widgets.DateInput(attrs={'type': 'date'})
        }


class ScheduleElementForm(forms.ModelForm):
    class Meta:
        model = ScheduleElement
        fields = [
            'presciption',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            'time'
        ]
        
        widgets = {
            'time': widgets.TimeInput(attrs={'type': 'time'})
        }