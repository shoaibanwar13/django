from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def ecom(request):
   products = Product.objects.all()
   return render(request, 'store/store.html', {'products':products})
def maine(request):
    return render(request,'store/maine.html')
def store(request):
    return render(request,'store/index.html')

# Create your views here.
