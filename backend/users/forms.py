from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Pseudo')
    #utilise le widget .PasswordInput qui cache automatiquement la saisie du mdp
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_photo']