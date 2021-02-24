from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='product'),
    path('search/', views.search, name='search'),
    path('<int:product_id>/product_description',views.product_description,name='product_description'),



]
