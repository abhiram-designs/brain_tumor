from django.shortcuts import render, redirect
from .models import Pmr
from doctor.models import Doctor
from datetime import date
import datetime
from user.models import User

def pmr(request,idd):
    ss=request.session["u_id"]
    mm=User.objects.get(us_id= idd)
    gg=Doctor.objects.get(doc_id=ss)
    d={
        'i':mm,
        'j':gg,
    }
    if request.method == "POST":
        oo=Pmr()
        oo.us_id= idd
        oo.doc_id= ss
        oo.date= datetime.datetime.today()
        oo.time= datetime.datetime.now()
        oo.pmr=request.POST.get("pmr")
        oo.save()
        
    return render(request, "pmr/pmr_reg.html",d)

def view_pmr(request):
    ss = request.session["u_id"]
    mm=User.objects.filter(us_id= ss)
    obj = Pmr.objects.filter(us_id=ss)
    v={
        'm' :obj,
        't':mm,
    }
    return render(request,"pmr/view_pmr.html",v)
