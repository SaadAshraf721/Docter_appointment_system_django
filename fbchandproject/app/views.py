from django.shortcuts import render
from PatientApp.models import User

# Create your views here.

def index(req):
    return render(req, 'index.html')









def appointments(req):
    return render(req, 'appointments.html')











def dashoardadmin(req):
    return render(req, 'admin/index.html ')






def appointmentlist(req):
    return render(req, 'admin/appointment-list.html ')


def patientlist(req):
    return render(req, 'admin/patient-list.html ')


def doctorlist(req):
    return render(req, 'admin/doctor-list.html ')