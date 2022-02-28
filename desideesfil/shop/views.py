from django.shortcuts import render
from django.shortcuts import get_object_or_404
from shop.models import Product
from . import models
# Create your views here.

def shop(request):
    shopView = Product.objects.all()   
    return render(request, 'shop/shop.html', {'shop':shopView})

def articleView(request, product_id):
    article = get_object_or_404(models.Product, id=product_id)
    return render(request, 'shop/article.html',{'article': article})