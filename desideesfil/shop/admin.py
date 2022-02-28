from django.contrib import admin
from shop.models import Category, Product, Status, Order, OrderLine

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(OrderLine)