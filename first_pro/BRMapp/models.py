from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    dpt=models.CharField(max_length=25)
    title=models.CharField(max_length=25)
    author=models.CharField(max_length=25)
    pbr=models.CharField(max_length=25)
    price=models.FloatField()
    def __str__(self):
        return self.title

class BRMuser(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    member_Id=models.CharField(max_length=15)
    def __str__(self):
        return self.member_Id
