from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Patient(models.Model):
    name = models.CharField(max_length=20, null=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Referral(models.Model):
    status = models.BooleanField(default=False)
    referral_code = models.CharField(unique=True, max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

