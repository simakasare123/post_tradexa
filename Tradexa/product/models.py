from django.db import models

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    price = models.FloatField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
   
    
    
    def __str__(self):
        return self.name
    
    

    
    
    
    

# Create your models here.
