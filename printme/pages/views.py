from django.shortcuts import render
from product.models  import Product
from order.models import Order

# Create your views here.

def index(request):
    product = Product.objects.order_by('-upload_date')
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


    return render(request, 'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')