from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    is_receptionist=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    is_hr=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)

class Appointments(models.Model):
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    doctor=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    username=models.CharField(max_length=100)

class Invoices(models.Model):
    paid=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    outstanding=models.CharField(max_length=100)
    username=models.CharField(max_length=100)


class MedicalHistory(models.Model):
    date=models.CharField(max_length=100)
    symptoms=models.CharField(max_length=100)
    prescription=models.CharField(max_length=100)
    username=models.CharField(max_length=100)

class Doctor(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    salary=models.IntegerField(default=0)

class Patient(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)