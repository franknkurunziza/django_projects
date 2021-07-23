from django.db import models
import re

class UserManager(models.Manager):
    def user_valid(self,postData):
        errors={}
        Email_Reg=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        users = User.objects.filter(email=postData['email'])

        if len(postData['first_name'])<2:
            errors['first_name']='FirstName can note be less than 2 character'

        if len(postData['last_name'])<2:
            errors['last_name']='LastName can note be less than 2 character'

        if not Email_Reg.match(postData['email']):
            errors['email']='Invalid Email adress!'

        if users:
            errors['unique']='Email has to be unique'

        if len(postData['password']) < 8 :
            errors['p_short']='Short Password'


        if postData['password'] != postData['conf_password']:
            errors['password']='Invalid Passsword or Mismatch '

        
        return errors
class WishManager(models.Manager):
    def wish_valid(self,postData):
        errors={}

        if len(postData['item'])<3:
            errors['item']='A Wish must consist of at least 3 characters!'

        if len(postData['description'])<3:
            errors['description']='The description must be provided!'


        return errors   




class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    #likeed_wishes many to many
    #user

class Wish(models.Model):
    item=models.CharField(max_length=50)
    description=models.TextField()
    wish_granted=models.BooleanField(default=False,null=True)
    wished_by=models.ForeignKey(User, related_name="wishes", on_delete=models.CASCADE)
    users_who_liked=models.ManyToManyField(User,related_name='liked_wishes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=WishManager()


