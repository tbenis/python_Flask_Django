from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):

    def validate_form(self, fname, lname, email,password, confpw):
        if len(fname) < 2:
            return False
        elif any(char.isdigit() for char in fname):
            return False
        else:
            return True

        if len(lname) < 4:
            return False
        elif any(char.isdigit() for char in lname):
            return False
        else:
            return True

        if len(email) < 1:
            return False
        elif not EMAIL_REGEX.match(email):
            return False
        else:
            return True

        if len(password) < 4:
            return False
        elif password != confpw:
            return False
        else:
            return True

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
