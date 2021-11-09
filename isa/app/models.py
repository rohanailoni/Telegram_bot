from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user(models.Model):
    userid=models.OneToOneField(User,on_delete=models.CASCADE)
    member=models.CharField(default="Faculty",max_length=20)
    
class Document(models.Model):
    user_acess=models.ForeignKey(User, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d',default="none")