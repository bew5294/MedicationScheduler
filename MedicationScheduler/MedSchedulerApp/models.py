from django.db import models
from AuthApp.models import Account
from django.core.validators import RegexValidator

# Create your models here.

class Medication(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ndc = models.CharField(verbose_name='National Drug Code', unique=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    dose = models.IntegerField(verbose_name='Dosage')
    strength = models.IntegerField(verbose_name='Strength (mg)')
    # interactions =\
        
    def __str__(self):
        return self.name


class Prescription(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    directions = models.TextField()
    quantity = models.IntegerField()
    refills = models.IntegerField()
    prescriber = models.CharField(max_length=50)
    scanned_label = models.ImageField(null=True, blank=True)
    date_filled = models.DateField()
    discard_after = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.medication.name


class Schedule(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class ScheduleElement(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    time = models.TimeField()
    is_taken = models.BooleanField(default=False)