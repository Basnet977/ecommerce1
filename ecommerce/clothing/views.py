from asyncio import ProactorEventLoop
from unicodedata import category
from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import Category,Product,About,Contact
from django.core.mail import send_mail
from django.contrib import messages

from rest_framework import serializers, viewsets
from .serializer import ProductSerializer

class ProductApiViews(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Create your views here.

def home(request):
    data = {
        'CategoryData': Category.objects.all()
    }
    return render(request,'pages/home/home.html',data)

def about(request):
    x = {
        'y': About.objects.all()
    }
    return render(request,'pages/about/about.html',x)

def products(request):
    data = {
        'CategoryData': Category.objects.all()
    }
    return render(request,'pages/products/products.html',data)

def contact(request):
    if request.method=="POST":
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject, message, email, ['tusarbasnet7@gmail.com'],fail_silently=False)
        messages.success(request,'SUCCESSFULLY DONE')
        Contact.objects.create(email=email,subject=subject,message=message)
        return redirect(request.META.get('HTTP_REFERRER'))
    else:
        return render(request,'pages/contact/contact.html')

def cat_display(request,cat_id):
    data = {
        'CategoryData': Category.objects.all(),
        'display': Product.objects.filter(cat_id = cat_id)
    }
    return render(request,'pages/cat_display/cat_display.html',data)

def product_details(request,slug):
    data = {
    'CategoryData': Category.objects.all(),
    'details':Product.objects.get(slug=slug)
    }
    return render(request,'pages/product_details/product-details.html',data)








