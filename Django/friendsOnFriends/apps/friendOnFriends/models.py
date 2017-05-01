from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Friendship(models.Model):
    p1 = models.ForeignKey(User, models.DO_NOTHING, related_name = 'p1')
    p2 = models.ForeignKey(User, models.DO_NOTHING, related_name = 'p2')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
