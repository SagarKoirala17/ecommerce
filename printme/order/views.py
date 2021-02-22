import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect,get_object_or_404

from .extras import generate_order_id
from account.models import Profile
from .models import Order,OrderItem
from product.models import Product
from django.urls import reverse

# Create your views here.

def get_user_pending_order(request):
    user_profile=get_object_or_404(Profile,user=request.user)
    order=Order.objects.filter(owner=user_profile,is_ordered=False)
    if order.exists():
        return order[0]
    return 0
@login_required()
def add_to_cart(request,**kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product=Product.objects.filter(id=kwargs.get('item_id','')).first()
    if product in request.user.profile.product.all():
        messages.error(request,'You already own this product')
        return redirect(reverse('product'))
    order_item, status=OrderItem.objects.get_or_create(product=product)
    user_order, status=Order.objects.get_or_create(owner=user_profile, is_ordered=True)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code=generate_order_id()
        user_order.save()

    messages.success(request,"Items sucessfully added on cart")
    return redirect(reverse('product'))

@login_required()
def delete_from_cart(request,item_id):
    item_to_delete=OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.success(request,"Order has been deleted")
    return redirect(reverse('order:order'))

@login_required()
def order_details(request,**kwargs):
    existing_order=get_user_pending_order(request)
    context={
        'order':existing_order
    }
    return render(request,'order/order.html',context)

@login_required()
def checkout(request):
    existing_order=get_user_pending_order(request)
    context={
        'order': existing_order

    }
    return render(request, 'order/check_out', context)
@login_required()
def process_payment(request,order_id):
    return redirect(reverse('order:update_records',
                            kwargs={
                                'order_id':order_id,
                            })
                    )
@login_required()
def update_transaction_records(request,order_id):
    order_to_purchase=Order.objects.filter(pk=order_id).first()
    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.datetime.now()
    order_to_purchase.save()
    order_items=order_to_purchase.items.all()
    order_items.update(is_ordered=True,date_ordered=datetime.datetime.now())
    #add order to the user profile
    user_profile=get_object_or_404(Profile,user=request.user)
    order_product=[item.product for item in order_items]
    user_profile.design.add(*order_product)
    messages.success(request,"Your items have been added to your list")
    return redirect(reverse('product'))

def success(request,**kwargs):
    return render(request,'order/success.html',{})