from itertools import product
from os import name
from django.conf import settings
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, default="Product")

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField()
    quantity = models.IntegerField()
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)

class Status(models.Model):
    name = models.CharField(max_length=255)

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    statusId = models.ForeignKey(Status, on_delete=models.CASCADE)
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class OrderLine(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()