from django.db import models

class User(models.Model):
    us_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    age = models.IntegerField()
    address = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    contact = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'
