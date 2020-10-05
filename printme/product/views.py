from django.shortcuts import render,get_object_or_404
from design.models import Design
from .models import Product
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def index(request):
    product=Product.objects.order_by('-upload_date')
    paginator = Paginator(product, 8)
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
# def create_design(request,product_id):
#     product=Product.objects.all()
#     design=Design.objects.all()
#     if product_id:
#         if request.method="POST":



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