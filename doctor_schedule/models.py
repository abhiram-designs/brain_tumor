from django.db import models
from doctor.models import Doctor 
from user.models import User


class DoctorSchedule(models.Model):
    sch_id = models.IntegerField(primary_key=True)
    # doc_id = models.IntegerField()
    doc=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    availability = models.IntegerField()
    date = models.CharField(max_length=45)
    start_time = models.CharField(max_length=45)
    end_time = models.CharField(max_length=45)
    av_date = models.CharField(max_length=11)
    class Meta:
        managed = False
        db_table = 'doctor_schedule'

class Appbk(models.Model):
    bk_id = models.AutoField(primary_key=True)
    # us_id = models.IntegerField()
    us=models.ForeignKey(User,on_delete=models.CASCADE)
    #doc_id = models.IntegerField()
    doc=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    sch=models.ForeignKey(DoctorSchedule,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    posted_date = models.DateField()
    posted_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'appbk'