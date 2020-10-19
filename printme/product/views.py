from django.shortcuts import render,get_object_or_404,redirect
from design.models import Design
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages
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


def create_design(request):
        products=Product.objects.all()
        if request.method == "POST":
              name = request.POST['name']
              description = request.POST['description']
              price = request.POST['price']
              product=request.POST['products']
              image=request.POST['image']
              is_published=request.POST['is_published']
              date=request.POST['date']
              if request.user.is_authenticated:
                  create_design=Design(name=name, price=price, products=products, image=image, is_published=is_published, date=date,description=description)
                  if create_design.is_published==True:
                    create_design.save()
                    messages.success(request, "Your design  has been submitted to the concerned one")
                    return redirect('product')
                  else:
                   messages.error(request,"You must enable is_published to publish the design first")
                   return redirect('create_design')
              else:
                messages.error(request,"You must login first to upload your design")
                return redirect('login')

        else:


           return render(request,"design/create_design.html")


def create(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }

    return render(request, 'design/create_design.html', context)


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