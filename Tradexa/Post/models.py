from django.db import models

from django.contrib.auth.models import User
from datetime import datetime


class User(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email   = models.EmailField()
    password= models.CharField(max_length=20)
   



    

       



class Post(models.Model):
    user = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)
   
    
    
    
    def __str__(self):
        return self.name
    
    

    
    
    
    

# Create your models here.
