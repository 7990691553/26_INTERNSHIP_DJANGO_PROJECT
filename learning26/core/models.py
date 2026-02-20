from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    #django user model has some default fields like username, email, password, first_name, last_name etc. we can add more fields to it by creating a custom user model and inheriting from AbstractUser
    roleChoice = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    )
    role = models.CharField(max_length=100,choices=roleChoice,null=True,blank=True)