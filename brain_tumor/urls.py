"""brain_tumor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from disease import views
from doctor import views as a
from doctor_schedule import views as b
from feedback import views as c
from homepage import views as d
from login import views as e
from chat import views as f
from pmr import views as g
from review import views as h
from user import views as i
from django.conf.urls import url

urlpatterns = [
    path('disease/',views.dis),
    path('viewdise/',views.vw_dis),
    path('vwdoc/',views.vw_doc),
    path('register/',a.reg),
    path('view/',a.view_doc),
    re_path("acc/(?P<idd>\w+)",a.accept),
    re_path("rej/(?P<idd>\w+)",a.reject),
    path('usvw_doc/',a.us_vw_doc),
    re_path(r'bookapp/(?P<idd>\w+)',b.book_app),
    path('viewapp/',b.view_app),
    path('docapp/',b.docapp),
    path('new_schedule/',b.post_schedule),
    path('viewsch/',b.viewdoc_schedule),
    path('usfeedback/',c.user_feedback),
    path('docfeedback/',c.doctor_feedback),
    path('viewfdbk/',c.view_feedback),
    path('homepage/',d.mainhome),
    path('userhomepg/',d.userhome),
    path('dochomepg/',d.dochome),
    path('adhomepg/',d.adhome),
    path('login/',e.login),
    re_path(r'pmr/(?P<idd>\w+)',g.pmr),
    path('vwpmr/',g.view_pmr),
    path('review/',h.post_review),
    path('viewrev/',h.view_review),
    path('vwrevw/',h.advw_reviews),
    path('ureg/',i.user_register),
    path('viewusr/',i.view_user),
    url('$',d.mainhome),
    path('chat/',include('chat.url'))
]

