from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='product'),
    path('<int:product_id>/design', views.design, name='design'),
    path('search/', views.search, name='search'),


]