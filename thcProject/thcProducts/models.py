from django.db import models

# Create your models here.
class Product(models.Model):
    prodId= models.AutoField(primary_key=True)
    prodTitle= models.CharField(max_length=50,default="")
    prodMarketPrice= models.IntegerField(default=0)
    prodThcPrice= models.IntegerField(default=0)
    prodCategory= models.CharField(max_length=50,default="")
    prodSubCategory= models.CharField(max_length=50,default="")
    productBrand= models.CharField(max_length=50,default="")
    prodDescription= models.CharField(max_length=500,default="")
    prodImage1= models.ImageField( upload_to='thcProducts/images',default="")
    prodImage2= models.ImageField( upload_to='thcProducts/images',default="")
    prodImage3= models.ImageField( upload_to='thcProducts/images',default="")
    prodImage4= models.ImageField( upload_to='thcProducts/images',default="")
    prodImage5= models.ImageField( upload_to='thcProducts/images',default="")
    prodVideoLink= models.CharField( max_length=500,default="")

    def __str__(self):
        return self.prodTitle

class Order(models.Model):
    orderId=models.AutoField(primary_key=True)
    products=models.CharField( max_length=1000)
    bill=models.CharField(max_length=1000000000000000000000000000000)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phoneNumber=models.CharField(max_length=50,default='')
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)