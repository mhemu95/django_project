from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200, default='-')
    category = models.CharField(max_length=100, default='-')
    date = models.CharField(max_length=10, default='-')
    short_text = models.TextField(default='-')
    quote_text = models.TextField(default='-')
    long_text = models.TextField(default='-')

    def __str__(self):
        return self.title
