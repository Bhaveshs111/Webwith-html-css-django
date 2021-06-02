from django.db import models
from django.contrib.auth.models import User



class Book(models.Model):
    dpt=models.CharField(max_length=25)
    title=models.CharField(max_length=25)
    author=models.CharField(max_length=25)
    pbr=models.CharField(max_length=25)
    price=models.FloatField()
    def __str__(self):
        return self.title