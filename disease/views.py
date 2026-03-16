from django.shortcuts import render, redirect
from .models import Disease
from user.models import User
from doctor.models import Doctor




def dis(request):
    if request.method == "POST":
        Disease.objects.create(
            name=request.POST.get("name"),
            symptoms=request.POST.get("symptoms"),
            status=request.POST.get("status"),
        )
        return redirect("/disease/")

    return render(request,"disease/dis_reg.html")


def vw_dis(request):
    ss=request.session["u_id"]
    mm=User.objects.filter(us_id=ss)
    dis = Disease.objects.all()
    return render(request, "disease/view_dis.html",{'d':dis,'k':mm})

def vw_doc(request):
    ss=request.session["u_id"]
    nn=Doctor.objects.filter(doc_id=ss)
    dis = Disease.objects.all()
    return render(request, "disease/doc_vwdis.html",{'d':dis,'l':nn})
