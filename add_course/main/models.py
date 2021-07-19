from django.db import models



class courseManager(models.Manager):
    def course_valid(self,postData):
        errors={}
        if len(postData['name']) < 5:
            errors['name'] = "Title should be at least 2 characters long"
        if len(postData['desc']) < 10:
            errors['desc'] = "Title should be at least 2 characters long"
        return errors

class Description(models.Model):
    desc=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Course(models.Model):
    name=models.CharField(max_length=50)
    desc=models.OneToOneField(Description, on_delete=models.CASCADE, primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=courseManager()





# Create your models here.
