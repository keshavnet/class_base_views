from django.db import models
from django import forms

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, default='')
