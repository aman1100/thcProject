from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Order
from django.contrib import messages

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
    if request.method == "POST":
        products = request.POST.get('products',"")
        bill = request.POST.get('bill',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phoneNumber = request.POST.get('phone',"")
        address1 = request.POST.get('address1',"")
        address2 = request.POST.get('address2',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zip = request.POST.get('zip',"")
        order=Order(products=products,bill=bill,name=name,email=email,phoneNumber=phoneNumber,address1=address1,address2=address2,city=city,state=state,zip=zip)
        order.save()
        messages.success(request,"Your order has been placed. Thank You for shopping with us :)")
        params={'done':True}
        return render(request,'thcProducts/checkOut.html',params)
        
    return render(request,'thcProducts/checkOut.html',)

def emptyCart(request):
    return render(request,'thcProducts/emptyCart.html')