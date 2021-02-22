from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
from product.models import Product
from datetime import datetime
# Create your models here.

class OrderItem(models.Model):
    product=models.OneToOneField(Product,on_delete=models.SET_NULL,null=True)
    is_ordered=models.BooleanField(default=False)
    date_added=models.DateTimeField(default=datetime.now)
    date_ordered=models.DateTimeField(default=datetime.now)

    def __str__(self):
        print (self.product)
        return self.product


class Order(models.Model):
    ref_code=models.CharField(max_length=15)
    owner=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    is_ordered=models.BooleanField(default=False)
    items=models.ManyToManyField(OrderItem)
    date_ordered=models.DateTimeField(default=datetime.now)

    def get_cart_items(self):
        return self.items.all()
    def get_cart_total(self):
        return([item.product.price for item in self.items.all()])
    def __self__(self):
        return '{0}-{1}'.format(self.owner,self.ref_code)