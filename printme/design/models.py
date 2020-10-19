from django.db import models
from datetime import datetime
from product.models import Product

# Create your models here.

class Design(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='photos/%Y/%m/%d/')
    price=models.IntegerField()
    is_published=models.BooleanField(default=True)
    date=models.DateTimeField(default=datetime.now)
    products=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Design"



