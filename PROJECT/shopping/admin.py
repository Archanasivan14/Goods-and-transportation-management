from django.contrib import admin
from . models import shop_tbl,product_tbl,cart_tbl,wishlist_tbl,address_tbl,order_tbl

# Register your models here.
admin.site.register(shop_tbl)
admin.site.register(product_tbl)
admin.site.register(cart_tbl)
admin.site.register(wishlist_tbl)
admin.site.register(address_tbl)
admin.site.register(order_tbl)
