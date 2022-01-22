from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from basic_app.models import UserProfileFieldInfo


##### classes

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileFieldInfoform(forms.ModelForm):
    class Meta():
        model = UserProfileFieldInfo
        fields = ('portfolio_site','profile_pic')
