from django.shortcuts import render, redirect
from .models import Review
from doctor.models import Doctor
from user.models import User
from datetime import date
import datetime
    
def post_review(request):
    ss=request.session["u_id"]
    l=Doctor.objects.all
    mm=User.objects.filter(us_id= ss)
    c={
        'j':l,
        'g':mm,
    }
    if request.method == "POST":
        p=Review()
        p.us_id=ss  
        p.doc_id = 1
        p.review = request.POST.get('review')
        p.date = datetime.datetime.today()
        p.time = datetime.datetime.now()
        p.save()

    return render(request,'review/us_review.html',c)

def view_review(request):
    ss=request.session["u_id"]
    tt=Doctor.objects.filter(doc_id=ss)
    review = Review.objects.filter(doc_id=ss)
    c={
        'k':review,
        'j':tt
    }
    return render(request, 'review/view_usreview.html',c)

def advw_reviews(request):
    review = Review.objects.all()
    c={
        'k':review
    }
    return render(request, 'review/adviewdoc_review.html',c)