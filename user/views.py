from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from login.models import Login

def user_register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        address = request.POST.get("address")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        password = request.POST.get("password")

        # Check email already exists in USER table
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("ureg/")  # URL name

        # Save user
        user = User.objects.create(
            name=name,
            gender=gender,
            age=age,
            address=address,
            email=email,
            contact=contact,
            password=password
        )

        # Save login credentials
        ob = Login()
        ob.username = email
        ob.password = password
        ob.u_id = user.us_id
        ob.type = 'user'
        ob.save()
        messages.success(request, "Registration successful. Please login.")
       # ✅ URL NAME (not path)

    return render(request, "user/user_reg.html")


def view_user(request):
    users = User.objects.all()
    return render(request, "user/view_user.html", {"users": users})
