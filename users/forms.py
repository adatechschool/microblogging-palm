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

AVATAR_CHOICES = [
    ('avatar1.png', 'Avatar 1'),
    ('avatar2.png', 'Avatar 2'),
    ('avatar3.png', 'Avatar 3'),
    ('avatar4.png', 'Avatar 4'),
    ('avatar5.png', 'Avatar 5'),
]

class EditProfileForm(forms.ModelForm):
    avatar_choice = forms.ChoiceField(
        choices=AVATAR_CHOICES,
        widget=forms.RadioSelect,
        label="Choisis ton avatar"
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar_choice']