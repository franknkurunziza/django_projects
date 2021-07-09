from django.db import models
from django.db.models.fields import CharField

class AuthorManager(models.Manager):
    def author_validator(self,postData):
        errors={}
        if len(postData['first_name']) <2:
            errors['first_name']="firstname must be long at least 3 character long"
        if len(postData['last_name']) <2:
            errors['last_name']="laststname must be long at least 3 character long"
        if len(postData['note']) <2:
            errors['note']="note must be long at least 3 character long"
        return errors

class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    notes=CharField(max_length=50,null=True)
    books=models.ManyToManyField(Book,related_name="authors")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=AuthorManager()
# Create your models here.
