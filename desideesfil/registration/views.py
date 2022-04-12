from django.shortcuts import render, redirect
from registration.forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from registration.models import User_address
from registration.models import Address, AddressCategory
from registration.forms import AddressForm, UserFormUpdate
from shop.models import Order, Product
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    """
        Return the signup page,
        with auto-complete of the adresses of user
    """
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():

            form.save()
            user = authenticate(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password1'])
            login(request, user)
            newAddressCategoryDelivery = AddressCategory(id = 1)
            newAddressCategoryBilling = AddressCategory(id = 2)
            newAddressDelivery = Address(address='', code=0, city='', addressCategoryName=newAddressCategoryDelivery, user_id=user.id)
            newAddressBilling = Address(address='', code=0, city='', addressCategoryName=newAddressCategoryBilling, user_id=user.id)
            newAddressDelivery.save()
            newAddressBilling.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    """
        Return the profile page, with information of user
    """
    userAddressDelivery = Address.objects.get(user_id = request.user.id, addressCategoryName_id = 1)
    userAddressBilling= Address.objects.get(user_id = request.user.id, addressCategoryName_id = 2)

    getOrders = Order.objects.filter(userId = request.user.id, statusId = 2)
    getProduct = Product.objects.all()

    context = {
        'user':request.user,
        'addressDelivery':userAddressDelivery,
        'addressBilling':userAddressBilling,
        'orders': getOrders,
        'product': getProduct,
        }
    return render(request, 'registration/profile.html', context)

def addressUpdateDelivery(request):
    """
        Return the update delivery address page,
        user can change or add delivery address
    """
    userAddress = Address.objects.get(user_id = request.user.id, addressCategoryName_id = 1 )
    if request.method == 'POST':
        formAddress = AddressForm(request.POST,instance=userAddress)
        if formAddress.is_valid():
            formAddress.save()
            return redirect('profile')
    else:
        formAddress = AddressForm(instance=userAddress)

    return render(request, 'registration/deliveryAddress.html', {'form': formAddress})

def addressUpdateBilling(request):
    """
        Return the update billing address page,
        user can change or add billing address
    """
    userAddress = Address.objects.get(user_id = request.user.id, addressCategoryName_id = 2)
    if request.method == 'POST':
        formAddress = AddressForm(request.POST,instance=userAddress)
        if formAddress.is_valid():
            formAddress.save()
            return redirect('profile')
    else:
        formAddress = AddressForm(instance=userAddress)

    return render(request, 'registration/billingAddress.html', {'form': formAddress})

def userUpdate(request):
    """
        Return the update information of user page,
        user can change basic information
    """
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
    """
        Return the delete account page,
        user can delete account on this page
    """
    getUser = User.objects.get(id = request.user.id)
    
    if request.method == 'POST':

        getUser.delete()

        return redirect('signup')

    return render(request, 'registration/delete.html', {'user': getUser})