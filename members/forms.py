from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username', 'class': "inputs_fields"}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password', 'class': "inputs_fields"}))
