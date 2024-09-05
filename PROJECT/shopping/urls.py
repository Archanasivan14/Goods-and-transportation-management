
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index),
    path('signin',views.signin),
    path('signout',views.signout),
    path('regform',views.regform),
    path('alldata',views.alldata),
    path('index',views.index),
    path('search',views.search),
    path('addtowishlist',views.addtowishlist),
    path('wishlist',views.wishlist),
    path('addtocart',views.addtocart),
    path('viewcart',views.viewcart),
    path('removefromcart',views.removefromcart),
    path('removefromwishlist',views.removefromwishlist),
    path('address',views.address),
    path('details',views.details),
    path('payment',views.payment),
    path('creditcard',views.creditcard),
    path('upi',views.upi),
    path('netbanking',views.netbanking),
    path('placed',views.placed),
    path('myorder',views.myorder),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#     
