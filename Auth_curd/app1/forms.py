from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from app1.models import Crud_model

class Signup(UserCreationForm):
    password2 = forms.CharField(label='confirm password (again)',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'emails':'Email'}



class Curd_form(ModelForm):
    class Meta:
        model = Crud_model
        fields = '__all__'