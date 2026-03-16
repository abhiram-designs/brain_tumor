from django.db import models

class Disease(models.Model):
    dis_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    symptoms = models.CharField(max_length=50)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'disease'
        
