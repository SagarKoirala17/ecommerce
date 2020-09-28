from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='product'),
    path('<int:product_id>', views.design, name='design'),



]