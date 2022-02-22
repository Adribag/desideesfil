from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registration.models import Address

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
        model = Address
        fields = ['address', 'code', 'city']