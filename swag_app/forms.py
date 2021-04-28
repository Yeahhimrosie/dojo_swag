# Marj: these will help our form process into the database
from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    zipcode = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
