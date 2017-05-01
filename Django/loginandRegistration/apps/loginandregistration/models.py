from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):

    def validate_form(self, fname, lname, email,password, confpw):
        errors = []
        valid = True
        if len(fname) < 2:

            errors.append('Your first name must have more than two characters')
            valid = False

        elif any(char.isdigit() for char in fname):

            errors.append('Your first name cannot contain a digit')
            valid = False
        if len(lname) < 2:

            errors.append('Your last name must have more than two characters')
            valid = False
        elif any(char.isdigit() for char in lname):

            errors.append('Your last name cannot contain a digit')
            valid = False
    

        if len(email) < 1:

            errors.append('Please enter a valid email')
            valid = False
        elif not EMAIL_REGEX.match(email):

            errors.append('Your email is invalid.. please enter something like: someone@example.something')
            valid = False

        if len(password) < 4:

            errors.append('Password must be greater than four characters')
            valid = False

        elif password != confpw:

            errors.append('Password and confirm password must match')
            valid = False

        if valid == True:
            return (True, errors)
        else:
            print "*"*50
            print errors
            print "*"*50

            return (False, errors)
    # def validate_login(self, request):





class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
