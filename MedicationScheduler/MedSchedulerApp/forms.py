from django import forms
from django.db.models import fields
from MedSchedulerApp.models import *


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = [
            'name',
            'ndc',
            'dose'
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
