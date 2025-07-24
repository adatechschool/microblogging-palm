from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='email de connexion')
    #utilise le widget .PasswordInput qui cache automatiquement la saisie du mdp
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')