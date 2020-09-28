from django.shortcuts import render
from product.models  import Product

# Create your views here.

def index(request):

    products = Product.objects.order_by('-upload_date')[:4]
    context={
        'products':products
    }

    return render(request, 'pages/index.html',context)