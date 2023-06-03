from django.db import models


class dialogue(models.Model):
    message = models.CharField(max_length=500)
    send_bot = models.BooleanField()
    send_date = models.DateTimeField(auto_now_add=True)


class QA(models.Model):
    user_input = models.CharField(max_length=500)
    bot_reply = models.CharField(max_length=500)
    

# Create your models here.
