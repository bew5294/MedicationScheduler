# Generated by Django 4.0 on 2022-01-19 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0003_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='caregiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AuthApp.account'),
        ),
    ]