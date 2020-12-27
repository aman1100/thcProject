from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products=Product.objects.all()
    params={'products':products}
    return render(request,'thcProducts/index.html',params)

def prodDetails(request,prodId):
    product=Product.objects.filter(prodId=prodId)
    params={'product':product[0]}
    #return HttpResponse('<h1>Page was found</h1>')
    return render(request,'thcProducts/productDetails.html',params)

def aboutus(request):
    return render(request,'thcProducts/aboutus.html')

def checkOut(request):
    return render(request,'thcProducts/checkOut.html')

def emptyCart(request):
    return render(request,'thcProducts/emptyCart.html')