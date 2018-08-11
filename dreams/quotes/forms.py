from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from . import models

class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={ 'placeholder': 'Username'}) )
	first_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'placeholder': 'First Name'}) )
	last_name =  forms.CharField(max_length=32,  widget=forms.TextInput(attrs={'placeholder': 'Last Name'}) )
	email 	  =  forms.EmailField(max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Email'}) )
	password1= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password Again'}))


	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
