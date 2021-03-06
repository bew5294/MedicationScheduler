# Generated by Django 4.0 on 2021-12-30 18:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AuthApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('ndc', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='National Drug Code')),
                ('dose', models.IntegerField(verbose_name='Dosage')),
                ('strength', models.IntegerField(verbose_name='Strength (mg)')),
            ],
        ),
        migrations.CreateModel(
            name='Presciption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directions', models.TextField()),
                ('quantity', models.IntegerField()),
                ('refills', models.IntegerField()),
                ('prescriber', models.CharField(max_length=50)),
                ('scanned_label', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_filled', models.DateField()),
                ('discard_after', models.DateField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AuthApp.account')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedSchedulerApp.medication')),
            ],
        ),
    ]
