# Generated by Django 4.1.5 on 2023-03-29 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_police_app', '0005_alter_emergencyinformationmodels_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitormodels',
            name='state',
        ),
    ]