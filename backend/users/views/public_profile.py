from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from users.models import User
from articles.models import Article

@login_required
def public_profile_view(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)

    # Articles de ce user
    articles = Article.objects.filter(user=profile_user).order_by('-created_at')

    return render(request, 'users/public_profile.html', {
        'profile_user': profile_user,
        'articles': articles,
    })
