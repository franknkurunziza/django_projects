from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters long"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters long"
        if len(postData['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters long"
        if len(postData['date']) < 10:
            errors['date'] = "Date should be at least 10 characters long!"
        if (postData['date']) >= datetime.now().strftime('%Y/%m/%d'):
            errors['date'] = "Date should be in the past!"
        shows = Show.objects.filter(title=postData['title'])
        if shows:
            errors['title'] = "title has to be unique!"
        return errors


    def update_validator(self, PostData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters long"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters long"
        if len(postData['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters long"
        if len(postData['date']) < 10:
            errors['date'] = "Date should be at least 10 characters long!"
        if (postData['date']) >= datetime.now().strftime('%Y/%m/%d'):
            errors['date'] = "Date should be in the past!"
        return errors



class Show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    date=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager()
# Create your models here.
