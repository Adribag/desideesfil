from django.shortcuts import render

# Create your views here.

def shop(request):
    context = {
        'title': "shop",
    }
    return render(request, 'shop/shop.html', context)