from django.shortcuts import render,get_object_or_404
from design.models import Design
from .models import Product
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def index(request):
    product=Product.objects.order_by('-upload_date')
    paginator = Paginator(product, 4)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'product': paged_products
    }


    return render(request,"product/product.html",context)

def design(request, product_id):
    product=Product.objects.all()
    designs=Design.objects.all()
    if product_id:
        product = get_object_or_404(Product, id=product_id)
        design=designs.filter(product=product)
        context = {
        'designs':designs,
        'design': design,
        'product':product,
    }
    return render(request, 'design/design.html', context)

