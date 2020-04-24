from django.db import models
from django.contrib.auth.models import User
class User(models.Model): 
    name = models.CharField(max_length=200) 
    email = models.CharField(max_length=200) 


class Organization(models.Model):  
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)) 


class Account(models.Model):  
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)