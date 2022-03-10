from itertools import product
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from shop.models import Product, OrderLine, Order, Status
from . import models
from django.contrib.auth.decorators import login_required
from shop.forms import addCart
from django.contrib.auth.models import User
from registration.models import Address
# Create your views here.

def shop(request):
    shopView = Product.objects.all()   
    return render(request, 'shop/shop.html', {'shop':shopView})

@login_required
def articleView(request, product_id):
    article = get_object_or_404(models.Product, id=product_id)
    getUser = User.objects.get(id = request.user.id)
    product = Product.objects.get(id = product_id)

    status = Status.objects.get(id = 1)

    if request.method == 'POST':
        form = addCart(request.POST)
        order = Order.objects.create(userId = getUser, statusId = status)
        orderLine = OrderLine.objects.create(orderId = order, quantity = 1, productId = product)
        if form.is_valid():
                        
            # form.save()
            
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
    getUser = User.objects.get(id = request.user.id)
    userAddress = Address.objects.get(user_id = request.user.id, addressCategoryName_id = 1)
    orders = Order.objects.filter(userId = getUser)
    orderLines = OrderLine.objects.filter(orderId__in = orders)

    context = {
        'user': getUser,
        'address': userAddress,
        'orderLines': orderLines,
        'orders': orders,
    }
    return render(request, 'shop/cart.html', context)


@login_required
def deleteArticle(request,id):
    orderLine = OrderLine.objects.get(id = id)

    if request.method == 'POST':
       

            print('delete')
            orderLine.delete()

            return redirect('shop:cart')

    context = {'orderLine': orderLine}

    return render(request,'shop/deleteArticle.html', context)