from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phonenumber = PhoneNumberField(widget=forms.TextInput(), label=("Phone number"), required=True)
    
    class Meta:
        model = User
        fields=['username','email','phonenumber','password1','password2']
