from django.db import models

from datetime import datetime


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    price = models.IntegerField()
    size=models.CharField(max_length=3,blank=True)
    color=models.CharField(max_length=100,blank=True)
    upload_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


