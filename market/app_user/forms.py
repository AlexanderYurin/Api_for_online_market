from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from app_user.models import Profile


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label=_('Login'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label=_('Password2'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label=_('Name'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label=_('Surname'), widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name',
                  'last_name')


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('balance',)
