from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user',)
    filter = ('user','product')
    search_fields = ('id','user',)
    list_per_page = 25


admin.site.register(Profile,ProfileAdmin)