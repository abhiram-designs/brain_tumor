from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Doctor
from login.models import Login
from user.models import User


def reg(request):
    if request.method == "POST":
        doctor=Doctor.objects.create(
            doc_name=request.POST.get("name"),
            gender=request.POST.get("gender"),
            dept = request.POST.get("dept"),
            qualification=request.POST.get("qualification"),
            experience=request.POST.get("experience"),
            email=request.POST.get("email"),
            contact=request.POST.get("contact"),
            password=request.POST.get("password"), 
            status="Pending"  
        )
        
        messages.success(request,"Registration submitted. Waiting for admin approval.")
        # obj=Doctor()
        ob = Login()
        ob.username = doctor.email
        ob.password = doctor.password
        ob.u_id = doctor.doc_id
        ob.type = 'doctor'
        ob.save() 
        return redirect("/login/") 

    return render(request, "doctor/doc_reg.html")


def accept(request,idd):
    obj=Doctor.objects.get(doc_id=idd)
    obj.status='approved'
    obj.save()
    return view_doc(request)

def reject(request,idd):
    obj=Doctor.objects.get(doc_id=idd)
    obj.status='rejected'
    obj.save()
    return view_doc(request)

def view_doc(request):
    ss = request.session["u_id"]
    doctors = Doctor.objects.all()
    mm=User.objects.filter(us_id= ss)
    return render(request,"doctor/view_doc.html",
        {"doctors": doctors,'h':mm}
    )
    
def us_vw_doc(request):
    ss = request.session["u_id"]
    mm = User.objects.filter(us_id=ss)
    doctors = Doctor.objects.filter(status='approved')
    return render(request,"doctor/us_view_doc.html",{"doctors": doctors,'h':mm})




