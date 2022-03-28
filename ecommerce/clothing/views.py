from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'pages/home/home.html')

def about(request):
    return render(request,'pages/about/about.html')

def contact(request):
    return render(request,'pages/contact/contact.html')

def products(request):
    return render(request,'pages/products/products.html')


