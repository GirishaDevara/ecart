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

