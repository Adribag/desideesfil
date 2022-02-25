from django.shortcuts import render, redirect
from main.forms import ContactForm
from main.models import Contact
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {
        'title': "Home",
        'user' : request.user
    }
    return render(request, 'main/index.html', context)


def contact(request):
    context = {
        'title': "Contact",
    }
    return render(request, 'main/contact.html', context)


def prices(request):
    context = {
        'title': "Prices",
    }
    return render(request, 'main/prices.html', context)


def contact(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            form.save()

            return redirect('/')

    context = {'form': form}
    return render(request, 'main/contact.html', context)
