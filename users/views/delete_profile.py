from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import logout

@login_required
def delete_profile_view(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home') 

    return render(request, 'users/confirm_delete.html')
