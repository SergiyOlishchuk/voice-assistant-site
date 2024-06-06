from dataclasses import fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "token",
            "password1",
            "password2",
        ]

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    token = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
            "token",
        ]
    
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    token = forms.CharField()

class UserChangePasswordForm(PasswordChangeForm):
        
    old_password = forms.CharField()
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()
    