from django import forms
from apps.payments.models import ProductOrder


class ProductOrderForm(forms.ModelForm):

    class Meta:
        model = ProductOrder
        fields = ['product', 'count']
        widgets = {
            'product': forms.HiddenInput(),
            'count': forms.HiddenInput()
        }


class ProductOrderUpdateForm(forms.ModelForm):

    class Meta:
        model = ProductOrder
        fields = ['order', 'product', 'count']
        widgets = {
            'order': forms.HiddenInput(),
            'product': forms.HiddenInput()
        }
