from django.shortcuts import render
from user.models import User
from chat.models import Chat
import datetime
from django.db.models import Q
from doctor.models import Doctor
# Create your views here.
from login.models import Login


def con(request):
    ss=request.session["u_id"]
    ob= Doctor.objects.all()
    obj=User.objects.get(us_id=ss)
    context={
        'u':ob,
        'k':obj
    }
    return render(request,'chat/viewcon.html',context)

def cochat(request,idd):
    ss=request.session["u_id"]
    obj = Doctor.objects.get(doc_id=idd)
    ob = Chat.objects.filter(Q(us_id=ss) & Q(doc_id=idd))
    context = {
        'kk': ob,
        'uu': obj,
    }
    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.doc_id=idd
        obk.us_id=ss
        obk.rectype="doctor"
        obk.sendertype = "user"
        obk.save()
    return render(request, 'chat/chatuser1.html',context)



def std(request):
    ss=request.session["u_id"]
    ob=User.objects.all()
    obj=Doctor.objects.get(doc_id=ss)
    context={
        'u':ob,
        'k':obj
    }
    return render(request,'chat/view user.html',context)


def stchat(request,idd):
    ss = request.session["u_id"]
    obj =User.objects.get(us_id=idd)
    ob=Chat.objects.filter(Q(us_id=idd) & Q(doc_id=ss))
    context={
        'kk':ob,
        'uu':obj,
    }

    if request.method=='POST':
        obk=Chat()
        obk.message=request.POST.get('mssg')
        obk.us_id=idd
        obk.doc_id=ss
        obk.rectype="user"
        obk.sendertype="doctor"
        obk.save()
    return render(request, 'chat/chatuser2.html',context)
