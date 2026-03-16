from django.db import models
from user.models import User
from doctor.models import Doctor

class Pmr(models.Model):
    pmr_id = models.AutoField(primary_key=True)
    #us_id = models.IntegerField()
    us=models.ForeignKey(User,on_delete=models.CASCADE)
    #doc_id = models.IntegerField()
    doc=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    pmr = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'pmr'

