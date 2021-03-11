from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','price','size','upload_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'upload_date', 'price')
    list_per_page = 25


admin.site.register(Product,ProductAdmin)
