from django.shortcuts import render, redirect
from .models import DoctorSchedule, Appbk
from doctor.models import Doctor
from datetime import date
import datetime
from user.models import User



def book_app(request,idd):
    ss=request.session["u_id"]
    aa=DoctorSchedule.objects.filter(doc_id=idd)
    ll=Doctor.objects.get(doc_id=idd)
    kk=User.objects.get(us_id=ss)
    c={
        'i':kk,
        'j':ll,
        'sss':aa
    }
    if request.method=='POST':
        obj = Appbk()
        obj.us_id = ss
        obj.doc_id = idd
        obj.sch_id = request.POST.get("schedule_id")
        obj.status = "Booked"
        obj.posted_date = datetime.datetime.today()
        obj.posted_time = datetime.datetime.now()
        obj.save()

    return render(request, "doctor_schedule/appointbk.html",c)


def view_app(request):
    ss = request.session["u_id"]
    mm=User.objects.filter(us_id= ss)
    obj = Appbk.objects.filter(us_id=ss)
    

    return render(request,"doctor_schedule/view_appointments.html",{'o': obj,'j':mm})


def docapp(request):
    ss = request.session["u_id"]
    mm=Doctor.objects.filter(doc_id=ss)
    obj = Appbk.objects.filter(doc_id=ss)

    return render(request,"doctor_schedule/docapp.html",{'o': obj,'j':mm})
    

def post_schedule(request):
    ss = request.session["u_id"] 
    mm = Doctor.objects.get(doc_id=ss)
    # login table u_id
    # doctor = Doctor.objects.get(doc_id=ss)  # get doctor row

    if request.method == "POST":
        availability = request.POST.get("availability")

        # current date of posting
        today_date = date.today()

        if availability == "yes":
            av_date = request.POST.get("av_date")
            start_time = request.POST.get("start_time")
            end_time = request.POST.get("end_time")

            dd=DoctorSchedule.objects.create(
                doc_id=ss,
                availability=True,
                av_date=av_date,
                start_time=start_time,
                end_time=end_time,
                date=today_date        # ✅ current posting date
            )
            dd.save()
        else:
            dd=DoctorSchedule.objects.create(
                doc_id=ss,
                availability=False,
                date=today_date        # ✅ current posting date
            )
            dd.save()
        return redirect("/new_schedule/")

    return render(request, "doctor_schedule/doc_schedule.html",{'j':mm})



def viewdoc_schedule(request):
    ss = request.session["u_id"]

    obj = DoctorSchedule.objects.all()

    return render(
        request,
        "doctor_schedule/viewdoc_schedule.html",
        {'o': obj}
    )



