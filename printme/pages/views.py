from django.shortcuts import render, redirect
from product.models import Product
from order.models import Order
from django.contrib import messages


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        product = Product.objects.order_by('-upload_date')[:4]
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

        return render(request, 'pages/index.html', context)
    else:
        messages.error(request, "Your Profile is not logged in yet")
        return redirect('login')


def about(request):
    return render(request, 'pages/about.html')
