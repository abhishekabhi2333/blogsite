from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class SigninForm(forms.Form):
    username=forms.CharField(max_length=120) 
    password=forms.CharField(max_length=120,widget=forms.PasswordInput())       