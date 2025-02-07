from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    prize = models.IntegerField()
    
class Customer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    