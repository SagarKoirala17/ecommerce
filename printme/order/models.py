from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
from product.models import Product
from datetime import datetime
import time


# Create your models here.

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(default=datetime.now)

    def __str__(self):
        title=self.product
        return str(title)


class Order(models.Model):

    timestamp = time.time()

    ref_code = models.CharField(max_length=255, default=timestamp)
    owner = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(default=datetime.now)


    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return ([items.product.price for item in self.items.all()])

    def __unicode__(self):
         return self.owner

