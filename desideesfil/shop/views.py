from itertools import product
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import F
from shop.models import Product, OrderLine, Order, Status
from . import models, forms
from django.contrib.auth.decorators import login_required
from shop.forms import addCart, CartValidation
from django.contrib.auth.models import User
from registration.models import Address

# Create your views here.

def shop(request):
    """
        Return the view of shop page, with all articles
        in database "Product"
    """
    shopView = Product.objects.all()  
    return render(request, 'shop/shop.html', {'shop':shopView})

@login_required
def articleView(request, product_id):
    """
        Return the view of an article
    """
    article = get_object_or_404(models.Product, id=product_id)
    getUser = User.objects.get(id = request.user.id)
    product = Product.objects.get(id = product_id)
    status = Status.objects.get(id = 1)

    if request.method == 'POST':
        form = addCart(request.POST)
        order = Order.objects.create(userId = getUser, statusId = status, productId = product, quantity = 1)
        orderLine = OrderLine.objects.create(orderId = order, quantity = 1, productId = product)
        
        if form.is_valid():

            if(product.quantity == 0):
                return render(request, 'shop/article.html', {'article': article, 'form': form})
            else:
                Product.objects.filter(id = product_id).update(quantity = product.quantity - 1)
                return redirect('shop:cart')
    else:
        form = addCart(instance = product, productId = product)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'shop/article.html',context)

@login_required
def cart(request):
    """
        Return the view of shop cart page,
        with articles of user
    """
    getUser = User.objects.get(id = request.user.id)
    userAddress = Address.objects.get(user_id = request.user.id, addressCategoryName_id = 1)
    orders = Order.objects.filter(userId = getUser)
    orderLines = OrderLine.objects.filter(orderId__in = orders)
    price = 0

    for orderLine in orderLines:
        price += orderLine.productId.price

    if request.method == 'POST':
        for orderLine in orderLines:
            getOrder = Order.objects.get(id = orderLine.orderId.id)
           
            if orderLine.orderId == getOrder:
                Order.objects.filter(id = orderLine.orderId.id).update(statusId=F('statusId')+1)
                orderLine.delete()
        
        return redirect('shop:cart')

    context = {
        'user': getUser,
        'address': userAddress,
        'orderLines': orderLines,
        'orders': orders,
        'price': price,
    }
    return render(request, 'shop/cart.html', context)

@login_required
def deleteArticle(request,id):
    """
        Return the remove page of an article in cart
    """
    orderLine = OrderLine.objects.get(id = id)
    product = Product.objects.get(id = orderLine.productId.id)
    if request.method == 'POST':
       
        orderLine.delete()
        Product.objects.filter(id = orderLine.productId.id).update(quantity = product.quantity + 1)
        return redirect('shop:cart')

    context = {'orderLine': orderLine}

    return render(request,'shop/deleteArticle.html', context)