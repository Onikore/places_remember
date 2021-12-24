from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import UserPosts


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'id': 'floatingInput'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'id': 'floatingPassword1'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'id': 'floatingPassword2'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AddUserPost(forms.ModelForm):
    title = forms.CharField(label='Заголовок',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'id': 'floatingInput'}))
    location = forms.CharField(label='Локация',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'id': 'floatingInput'}))
    description = forms.CharField(label='Описание',
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control',
                                             'id': 'floatingInput'}))

    class Meta:
        model = UserPosts
        fields = ('title', 'location', 'description')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'id': 'floatingInput'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control',
                                          'id': 'floatingPassword'}))
