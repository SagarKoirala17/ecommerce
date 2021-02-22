import random
import string
import string
from datetime import date
import datetime
from .models import OrderItem

def generate_order_id():
    date_str=date.today().strftime('%Y%m%d'[2:]+str(datetime.datetime.now()+seconds))
    rand_str=""+join([random.choice(string.digits) for count in range[3]])
    return date_str + rand_str

def get_reference_code():
    rand_str=""+([random.choice[string.digits] for count in range[3]])
    return rand_str
