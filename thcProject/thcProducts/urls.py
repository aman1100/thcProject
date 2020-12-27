from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='Home'),
    path('aboutus/',views.aboutus,name='aboutUs'),
    path('product/<int:prodId>',views.prodDetails,name='prodDetails'),
    path('emptyCart/',views.emptyCart,name='emptyCart'),
    path('checkOut/',views.checkOut,name='checkOut'),
    
]