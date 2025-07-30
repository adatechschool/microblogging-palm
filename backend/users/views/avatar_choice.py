from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from avatarForms import AvatarChoiceForm

@login_required
def choose_avatar(request):
    user = request.user
    if request.method == 'POST':
        form = AvatarChoiceForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # ou la page de ton choix
    else:
        form = AvatarChoiceForm(instance=user)
    
    return render(request, 'choose_avatar.html', {'form': form})