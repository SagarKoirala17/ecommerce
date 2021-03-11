from django.shortcuts import render, get_object_or_404, redirect
from order.models import Order

from .models import Product


# Create your views here.

def index(request):
  if request.user.is_authenticated:
    product = Product.objects.order_by('-upload_date')
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
  else:
    return redirect('login')

def product_description(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=True)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'product': product,
        'current_order_products': current_order_products
    }
    return render(request,"product/productDetail.html",context)


def search(request):
    queryset_list=Product.objects.order_by('-upload_date')
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=True)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    if 'products' in request.GET:
        products=request.GET['products']
        if products:
            queryset_list=queryset_list.filter(name__icontains=products)


    context={
        'product': queryset_list,
        'values': request.GET,
        'current_order_products': current_order_products

    }
    return render(request,'product/search.html',context)
