from django.shortcuts import render, redirect
from .models import Feedback
from user.models import User 
from doctor.models import Doctor
import datetime


def user_feedback(request):
    ss=request.session["u_id"]
    mm=User.objects.filter(us_id=ss)
    d={
        'i':mm
    }
    
    if request.method == "POST":
        p=Feedback()
        p.us_id=ss
        p.role = 'user'
        p.feedback = request.POST.get('feedback')
        p.date= datetime.datetime.today()
        p.save()

    return render(request,'feedback/us_feedback.html',d)


def doctor_feedback(request):
    ss=request.session["u_id"]
    mm=Doctor.objects.filter(doc_id=ss)
    c={
        "i":mm
    }
    if request.method == "POST":
            p=Feedback()
            p.doc_id=ss
            p.role = 'doctor'
            p.feedback= request.POST.get('feedback')
            p.date= datetime.datetime.today()
            p.save()

    return render(request, 'feedback/doc_feedback.html',c)

def view_feedback(request):
    fd = Feedback.objects.filter(role = 'user')
    fs = Feedback.objects.filter(role = 'doctor')
    v={
        'm' :fd,
        'n' :fs,
        }

    return render(request, 'feedback/view_feedback.html',v)