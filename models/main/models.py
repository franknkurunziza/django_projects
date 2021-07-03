from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    alias=models.TextField()
    age=models.IntegerField() 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)