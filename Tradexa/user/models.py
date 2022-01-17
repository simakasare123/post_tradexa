from django.db import models

class Product(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    
   
    
    
    def __str__(self):
        return self.username
    
    

    
    
    
    

# Create your models here.
