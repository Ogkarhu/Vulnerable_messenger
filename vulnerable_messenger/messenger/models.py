from django.db import models

    
    
class User(models.Model):
    name = models.CharField()
    user_id = models.IntegerField()
    isadmin = models.BooleanField(default=False)
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.IntegerField()
    msg_id = models.IntegerField()
    message = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
