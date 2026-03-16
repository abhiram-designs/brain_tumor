from django.shortcuts import render, HttpResponseRedirect
from login.models import Login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        obj = Login.objects.filter(username=username,password=password)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid= ob.u_id
            if tp == "admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/adhomepg/')
            elif tp == "user":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/userhomepg/')
            elif tp == "doctor":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/dochomepg/')
            else:
                objlist = "username or password incorrect.....please try again...."
                context = {
                    'k': objlist
                }
            return render(request,'login/login.html',context)
    return render(request,'login/login.html')

