from django.contrib import admin
from .models import Product, Cart, Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=["userid","productid","productname","category","desc","price","photos"]


class CartAdmin(admin.ModelAdmin):
    list_display=["userid","productid","qty"]


class OrderAdmin(admin.ModelAdmin):
    list_display=["userid","productid","orderid","qty"]

admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)
