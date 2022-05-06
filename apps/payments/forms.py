from django import forms
from apps.payments.models import ProductOrder
from apps.products.models import ProductStore


class ProductOrderForm(forms.ModelForm):

    class Meta:
        model = ProductOrder
        fields = ['product', 'count']
        widgets = {
            'product': forms.HiddenInput(),
            'count': forms.HiddenInput()
        }


class ProductOrderUpdateForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data['product']
        if cleaned_data['count'] > product.total_quantity:
            raise forms.ValidationError(f'очень много. Нельзя больше {product.total_quantity}')
        return cleaned_data

    class Meta:
        model = ProductOrder
        fields = ['order', 'product', 'count']
        widgets = {
            'order': forms.HiddenInput(),
            'product': forms.HiddenInput()
        }
