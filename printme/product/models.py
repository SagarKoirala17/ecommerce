from django.core.exceptions import ValidationError
from django.db import models

from datetime import datetime


def minpricevalidator(value):
    if value > 0:
        return True
    else:
        raise ValidationError("Price must be greator than 0")


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    price = models.FloatField(validators=[minpricevalidator])
    size = models.CharField(max_length=3, blank=True)
    color = models.CharField(max_length=100, blank=True)
    upload_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
