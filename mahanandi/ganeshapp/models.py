from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect


class Employee(models.Model):
    ename = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    esalary = models.FloatField()
    edate = models.DateField(auto_now=True)
    status = models.BooleanField(default=1)
    createdby=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
