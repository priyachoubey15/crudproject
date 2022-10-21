from django.db import models


# Create your models here.

class crud(models.Model):
    name=models.CharField(max_length=15)
    roll=models.IntegerField()
    city=models.CharField(max_length=15)