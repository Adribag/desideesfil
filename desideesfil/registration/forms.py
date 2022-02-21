from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registration.models import User_address

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserFormUpdate(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class AddressForm(forms.ModelForm):

    class Meta:
        model = User_address
        fields = ['delivery_address', 'delivery_code', 'delivery_city', 'billing_address','billing_code','billing_city']