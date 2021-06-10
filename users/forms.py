from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields 
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from users.models import Profile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model           = User
        fields          = ['username' , 'email' , 'password1' , 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model           = User
        fields          = ['username' , 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model           = Profile
        fields          = ['image']
