from django.db import models

# Create your models here.
class signupmodels(models.Model):

    role = models.CharField(max_length=30)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    password = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField(default=78945613)

class visitormodels(models.Model):
     
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    city = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    visitdate = models.DateTimeField(blank=True)

class contactusmodels(models.Model):

    username = models.EmailField()
    mobile = models.BigIntegerField()
    comments = models.TextField()

class emergencyinformationmodels(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()
    address = models.TextField()
    file = models.FileField(upload_to='upload')

class complationmodels(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    city = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    address = models.TextField()
    complaintdate = models.DateTimeField(blank=True)

class searchpolicestationmodels(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    policestationname = models.CharField(max_length=30)

class givefeedbackmodels(models.Model):  

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()
    comments = models.TextField()

class firmodels(models.Model):                            

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()
    firdate = models.DateTimeField(blank=True)