from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Main(models.Model):
    name = models.CharField(default='-', max_length=100)
    about = models.TextField(default='-')
    phone = models.CharField(max_length=15, default='-')
    email = models.EmailField(default='-')
    address = models.CharField(max_length=200, default='-')
    facebook = models.CharField(max_length=200, default='-')
    twitter = models.CharField(max_length=200, default='-')
    instagram = models.CharField(max_length=200, default='-')
    skype = models.CharField(max_length=200, default='-')

    def __str__(self):
        return self.name + ' | ' + str(self.pk)
