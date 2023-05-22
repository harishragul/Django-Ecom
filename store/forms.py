from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Require, Shop, Product, OrderItem

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'username'})
        self.fields['password1'].widget.attrs.update({'id': 'pw1'})
        self.fields['password2'].widget.attrs.update({'id': 'pw2'})
        self.fields['email'].required = True

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'number']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs.update({'id': 'mobile'})

class RequireForm(ModelForm):
    class Meta:
        model = Require
        fields = ['customer', 'product', 'category', 'image', 'image_2', 'file', 'description']

    def __init__(self, *args, **kwargs):
        super(RequireForm, self).__init__(*args, **kwargs)
        name = ['product', 'category', 'description']
        for i in name:
            self.fields[i].widget.attrs.update({
                'class': 'input',
                'placeholder': i})

class DealerForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'number', 'shop_identity', 'address', 'city', 'state', 'zipcode']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'old_price', 'image1', 'image2', 'image3', 'image4', 'description', 'details', 'shop', 'category']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        name = ['name', 'price', 'old_price', 'description', 'details', 'shop', 'category']
        for i in name:
            self.fields[i].widget.attrs.update({
                'class': 'input',
                'placeholder': i})

class PackForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['packed', 'shipped']

class ShipStatusForm2(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['out_for_delivery']

class ShipStatusForm3(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['delivered']
