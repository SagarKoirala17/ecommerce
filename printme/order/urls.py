from django.conf.urls import url
from .views import (
add_to_cart,
delete_from_cart,
order_details,
checkout,
process_payment,
update_transaction_records,
success
)
app_name='order'
urlpatterns=[
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$',add_to_cart,name="add_to_cart"),
    url(r'^order-summary/$',order_details,name="order_details"),
    url(r'^item/delete(?P<item_id>[-\w]+)/$',delete_from_cart,name="delete_from_cart"),
    url(r'^success/$',success,name="success"),
    url(r'^payment/(?P<order_id>[-\w]+)/$',process_payment,name="process_payment"),
    url(r'^update-transaction/(?P<item_id>[-\w]+)/$',update_transaction_records,name="update_records"),


]