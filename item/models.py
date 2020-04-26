from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    image_url = models.CharField(max_length=2083)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    yourname = models.CharField(max_length=5)
    mailid = models.EmailField()
    subject = models.CharField(max_length=5)
    body = models.CharField(max_length=5)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True,null=True)
    language_choices = (
        ('T', 'Telugu'),
        ('E', 'English'),
        ('H', "Hindi"),
    )
    language = models.CharField(max_length=1, choices=language_choices,blank=True,null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.yourname
