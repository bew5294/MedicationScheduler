# Generated by Django 4.0 on 2022-01-09 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MedSchedulerApp', '0003_rename_account_presciption_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduleelement',
            old_name='presciption',
            new_name='prescription',
        ),
    ]
