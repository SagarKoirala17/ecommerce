from django.shortcuts import render,get_object_or_404,redirect

from .models import Product

from order.models import Order
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from account.models import Profile



# Create your views here.


def index(request):
    product = Product.objects.order_by('-upload_date')[':4']
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=True)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context={
        'product':product,
        'current_order_products': current_order_products

    }
    return render(request, "product/product.html", context)





def search(request):
    queryset_list=Product.objects.order_by('-upload_date')
    if 'products' in request.GET:
        products=request.GET['products']
        if products:
            queryset_list=queryset_list.filter(name__icontains=products)


    context={
        'product': queryset_list,
        'values': request.GET

    }
    return render(request,'product/search.html',context)
