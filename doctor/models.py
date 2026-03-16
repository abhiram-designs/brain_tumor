from django.db import models


class Doctor(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    dept = models.CharField(max_length=45)
    qualification = models.CharField(max_length=45)
    experience = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    contact = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'doctor'
