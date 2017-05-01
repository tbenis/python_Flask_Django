from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from datetime import datetime
from datetime import date


lettersOnly = re.compile(r'^[a-zA-Z]*$')
emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class userManager(models.Manager):
    def rValidate(self, postData):
        errors = []
        flag = False
        if not postData['fname']:
            errors.append('First name must not be blank.')
            flag = True
        if len(postData['fname']) < 3:
            errors.append('First name must be at least 3 characters.')
            flag = True
        if not lettersOnly.match(postData['fname']):
            errors.append('First name must not contain numbers.')
            flag = True
        if not postData['lname']:
            errors.append('Last name must not be blank.')
            flag = True
        if len(postData['lname']) < 3:
            errors.append('Last name must be at least 3 characters.')
            flag = True
        if not lettersOnly.match(postData['lname']):
            errors.append('Last name must not contain numbers.')
            flag = True
        if not emailRegex.match(postData['email']):
            errors.append('Email address was not valid.')
            flag = True
        if not postData['email']:
            errors.append('Email must not be blank.')
            flag = True
        if not postData['password']:
            errors.append('Password must not be blank.')
            flag = True
        if postData['password'] != postData['cPassword']:
            errors.append('Passwords must match.')
            flag = True
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters long.')
            flag = True

        if not flag:
            # Encrypt password
            hashedPw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            # Save to database
            if User.objects.create(
                first_name=postData['fname'],
                last_name=postData['lname'],
                email=postData['email'],
                password=hashedPw
                ):
                print "Reg success"
                user = User.objects.last()
                return(flag, user)
            else:
                print "Reg failed"
        return(flag, errors)

    def lValidate(self, postData):
        user = User.objects.get(email=postData['email'])
        password = postData['password'].encode()
        hashed = user.password.encode()

        if bcrypt.hashpw(password, hashed) == hashed:
            return (True, user)
        else:
            return (False, "Login credentials are invalid.")
class TripManager(models.Manager):
    def validateTrip(self, postData):
        print "8"*50
        try:
            flag = False
            errors = []
            if not postData['destination']:
                errors.append('Please enter a Destination')
                flag = True
            if not postData['description']:
                errors.append('Please enter a Description')
                flag = True
            if not postData['from']:
                errors.append('Please enter a Travel Date')
                flag = True
            if not postData['till']:
                errors.append('Please enter Return Date')
                flag = True

        except:
            return False
        if flag:
            # print "7"*50
            # print errors
            return (flag, errors)
        else:
            Trip.objects.create(destination = postData['destination'], description = postData['description'], travel_date = postData['from'], return_date = postData['till'])
            # print "8"*50
            last = Trip.Objects.last()
            print "Trip created"
            return (flag, last)

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, )
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = userManager()

class Trip(models.Model):
    destination = models.TextField(max_length= 1000)
    description = models.TextField(max_length= 1000)
    travel_date = models.TextField(max_length= 1000)
    return_date = models.TextField(max_length= 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripManager()
    users = models.ManyToManyField(User)
