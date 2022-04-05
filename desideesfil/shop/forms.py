from dataclasses import fields
from django import forms
from shop.models import OrderLine

class addCart(forms.ModelForm):

    class Meta:
        model = OrderLine
        fields = ['productId']
        widgets = {
            'productId': forms.HiddenInput(),
            # 'categoryId': forms.HiddenInput()
            }

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('productId', None)
        super().__init__(*args, **kwargs)

        self.fields['productId'].widget.attrs['value'] = product.id if product is not None else '0'


class CartValidation(forms.Form):
    validation = forms.BooleanField(widget=forms.HiddenInput, initial=True)