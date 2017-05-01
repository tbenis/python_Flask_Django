from __future__ import unicode_literals
from django.db import models
import re , bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
allwords = re.compile(r'^[a-zA-z]*$')

# Create your models here.
class userManager(models.Manager):
    try:
        def validReg(self, postData):
            errors =[]
            flag = False
            if len(postData['fname']) < 2:
                errors.append("Your firstname Must be more than two characters ")
                flag = True
            if not allwords.match(postData['fname']):
                errors.append("Your First Name cannot contain a number")
                flag = True
            if len(postData['lname']) < 2:
                errors.append("Your Last Name Must be more than two characters ")
                flag = True
            if not allwords.match(postData['lname']):
                errors.append("Your Last Name cannot contain a number")
                flag = True
            if not EMAIL_REGEX.match(postData['email']):
                errors.append('Invalid Email')
                flag = True
            if len(postData['pw'])< 2:
                errors.append('Your password must be more than 8 characters')
                flag = True
            if postData['pw'] != postData['cpw']:
                errors.append('Your passwords must match')
                flag = True
            if flag:
                return (flag, errors)
            if not flag:
                hashedPw = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt())
                User.objects.create(first_name= postData['fname'], last_name=postData['lname'], email =postData['email'], password=hashedPw)
                currUser =  User.objects.last()
                return (flag, currUser)
    except:
        print "Hey"

class User(models.Model):
    first_name =models.CharField(max_length = 45)
    last_name =models.CharField(max_length = 45)
    email =models.CharField(max_length = 45, unique=True)
    password =models.CharField(max_length = 255)
    created_at =models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = userManager()
