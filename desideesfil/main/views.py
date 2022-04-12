from django.shortcuts import render, redirect
from main.forms import ContactForm
from main.models import Contact
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    """
        Return the index page,
        the main page of web site
    """
    context = {
        'title': "Home",
        'user' : request.user
    }
    return render(request, 'main/index.html', context)

def prices(request):
    """
        Return the prices page, 
        user can see different prices on this page
    """
    context = {
        'title': "Prices",
    }
    return render(request, 'main/prices.html', context)

def contact(request):
    """
        Return the contact form page,
        user can send a message to the admin
    """
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            form.save()

            return redirect('/')

    context = {'form': form}
    return render(request, 'main/contact.html', context)
