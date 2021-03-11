from django.contrib import admin
from .models import OrderItem,Order
# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product','date_ordered')
    list_display_links = ('product','date_ordered')
    search_fields = ('product',)
    list_per_page=25
class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner','ref_code','date_ordered','is_ordered')
    list_display_links = ('owner','ref_code')
    search_fields = ('owner','ref_code')
    list_editable = ('is_ordered',)
    list_per_page = 25

admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Order,OrderAdmin)