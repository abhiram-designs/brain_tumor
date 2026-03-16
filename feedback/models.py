from django.db import models
from doctor.models import Doctor
from user.models import User

class Feedback(models.Model):
    f_id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=10)
    feedback = models.CharField(max_length=45)
    #us_id = models.IntegerField()
    us=models.ForeignKey(User,on_delete=models.CASCADE)
    #doc_id = models.IntegerField()
    doc=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'feedback'