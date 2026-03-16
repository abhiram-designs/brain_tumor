from django.shortcuts import render
from user.models import User
from doctor.models import Doctor

def adhome(request):
    return render(request,'homepage/admin_home.html')

def dochome(request):
    ss = request.session['u_id']
    mm=Doctor.objects.filter(doc_id=ss)
    d={
        'i':mm
    }
    return render(request,'homepage/doc_home.html',d)

def userhome(request):
    ss = request.session['u_id']
    mm=User.objects.filter(us_id=ss)
    d={
        'i':mm
    }
    return render(request,'homepage/user_home.html',d)

def mainhome(request):
    return render(request,'homepage/main_home.html')