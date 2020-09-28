from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        message=request.POST['message']
        email=request.POST['email']

        context={
            'contact':contact
        }


        return render(request,'contact/contact.html',context)