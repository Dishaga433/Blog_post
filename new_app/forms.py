from django import forms
from django.contrib.auth.forms import UserCreationForm

from new_app.models import Login, Seller, Customer, Blog


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password=forms.CharField(label="password",widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ("username","password")


class SellerRegistration(forms.ModelForm):
    class Meta:
        model=Seller
        fields="__all__"
        exclude=("user",)


class CustomerRegistration(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        exclude=("user",)



class Blogging(forms.ModelForm):
    class Meta:
        model=Blog
        fields ="__all__"
        exclude=("seller_name",)