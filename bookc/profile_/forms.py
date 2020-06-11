from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Обязательное поле')
#   phone = forms.CharField(label='Телефон')
#   avatar = forms.ImageField(label='Аватар')
  class Meta:
     model = User
     fields = ('username', 'email', 'password1', 'password2')