from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import User, Patient, Referral
from patient import utils
from datetime import datetime

import africastalking

username = "dnz"
api_key = "b8dc628ebf993960e1ed3db79a9f1bb24520969fbd02d84536b92123c405902c"
africastalking.initialize(username, api_key)

sms = africastalking.SMS


def send_sms(message, phone_number):
    response = sms.send(message, phone_number)
    print(response)


# Create your views here.
class PatientListView(ListView):
    model = Patient
    context_object_name = 'posts'
    template_name = 'users/home.html'


def homePage(request):
    return render(request, 'patient/index.html', {
        "code": utils.create_referal_code()
    })


def add_referral(request):
    if request.method == 'POST':
        name = request.POST.get('patient_name')
        age = request.POST.get('age')
        number = request.POST.get('patient_number')
        doctor = request.user

        reason = request.POST.get('reason_for_referral')

        patient = Patient.objects.create(
            name=name,
            age=age,
            phone_number=number,
        )

        referral = Referral.objects.create(
            referral_code=utils.create_referal_code(),
            patient=patient,
            doctor=doctor,
            diagnosis=reason,
            date_posted=datetime.now(),
        )

        send_sms(f"Dear {patient.name} you referral code is {referral.referral_code}", [number])
        return redirect('home')
    elif request.method == 'GET':
        return render(request, 'patient/add_referral.html')
    else:
        return HttpResponse()
