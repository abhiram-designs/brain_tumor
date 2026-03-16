from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100)
    doc_id = models.IntegerField()
    us_id = models.IntegerField()
    sendertype = models.CharField(max_length=45)
    rectype = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'chat'




