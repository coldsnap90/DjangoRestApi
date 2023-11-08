from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class Student(AbstractUser):
    id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    last_login = models.CharField(max_length=100,blank=True,null=True)
    is_superuser = models.CharField(max_length=100) # ↓ Here
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    is_staff = models.CharField(max_length=100,default=True)
    is_active = models.CharField(max_length=100,default=True)
    date_joined = models.CharField(max_length=100,default = datetime.date.today())


    class Meta:
        ordering = ['id']