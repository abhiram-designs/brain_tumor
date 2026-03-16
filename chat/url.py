from django.conf.urls import url
from chat import views

urlpatterns=[
    url('nur/',views.con),
    url('con/(?P<idd>\w+)',views.cochat),

    url('usr/',views.std),
    url('std/(?P<idd>\w+)',views.stchat),

]