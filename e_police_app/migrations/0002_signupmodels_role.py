# Generated by Django 4.1.5 on 2023-03-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_police_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupmodels',
            name='role',
            field=models.CharField(default='', max_length=20),
        ),
    ]
