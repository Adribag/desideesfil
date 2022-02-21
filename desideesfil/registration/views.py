from django.shortcuts import render, redirect
from registration.forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from registration.models import User_address
from registration.forms import AddressForm, UserFormUpdate
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # User_address.objects.create(user_id = id)
            
            form.save()
            user = authenticate(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password1'])
            login(request, user)
            newAddress = User_address(delivery_address='', delivery_code=0, delivery_city='', billing_address='', billing_code=0, billing_city='', user_id=user.id)
            newAddress.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@login_required
def profile(request):
    # user = User.objects.all()
    context = {
        'user':request.user,
        'address':request.user.user_address
        }
    return render(request, 'registration/profile.html', context)


def addressUpdate(request):
    userAddress = User_address.objects.get(user = request.user.id)
    if request.method == 'POST':
        formAddress = AddressForm(request.POST,instance=userAddress)
        if formAddress.is_valid():
            formAddress.save()
            return redirect('profile')
    else:
        formAddress = AddressForm(instance=userAddress)

    return render(request, 'registration/address.html', {'form': formAddress})


def userUpdate(request):

    getUser = User.objects.get(id = request.user.id)

    if request.method == 'POST':
        userUpdate = UserFormUpdate(request.POST, instance=getUser)
        if userUpdate.is_valid():
            userUpdate.save()
            return redirect('profile')
    
    else:
        userUpdate = UserFormUpdate(instance=getUser)

    return render(request, 'registration/user.html', {'form': userUpdate})

def userDelete(request):

    getUser = User.objects.get(id = request.user.id)
    
    if request.method == 'POST':

        getUser.delete()

        return redirect('signup')

    return render(request, 'registration/delete.html', {'user': getUser})