from django.shortcuts import render

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