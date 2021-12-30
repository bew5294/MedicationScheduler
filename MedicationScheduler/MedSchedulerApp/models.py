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


class Presciption(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
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


# class ScheduleElement(models.Model):
#     TIMES = (
#         ('Morning', '09:00:00'),
#         ('Midday',  '12:00:00'),
#         ('Evening', '19:00:00'),
#         ('Bedtime', '22:00:00')
#     )
#     presciption = models.ForeignKey(Presciption, on_delete=models.CASCADE)
    
#     time = models.TimeField()
#     is_taken = models.BooleanField(default=False)