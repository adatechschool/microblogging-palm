from .. import forms
from django.contrib.auth import login, authenticate, logout 
from django.shortcuts import render, redirect

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('accueil')
        message = 'Identifiants invalides !'
    return render(
        request, 'users/login.html', context={'form': form, 'message': message})

def logout_user(request):

    logout(request)
    return redirect('login')
    