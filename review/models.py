from django.db import models
from user.models import User
from doctor.models import Doctor

class Review(models.Model):
    re_id = models.AutoField(primary_key=True)
    # us_id = models.IntegerField()
    us=models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    # doc_id = models.IntegerField()
    doc=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'review'
