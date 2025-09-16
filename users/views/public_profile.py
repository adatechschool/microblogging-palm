from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from users.models import User
from articles.models import Article
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseNotAllowed,
)

# @login_required
# def public_profile_view(request, user_id):
#     profile_user = get_object_or_404(User, id=user_id)

#     # Articles de ce user
#     articles = Article.objects.filter(user=profile_user).order_by('-created_at')

#     return render(request, 'users/public_profile.html', {
#         'profile_user': profile_user,
#         'articles': articles,
#     })

@login_required
def public_profile(request: HttpRequest, user_id: int) -> HttpResponse:
    profile_user = get_object_or_404(User, id=user_id)
    articles = profile_user.articles.all() # type: ignore[attr-defined]
    liked_articles = Article.objects.filter(liked_by=profile_user).order_by('-created_at') # type: ignore[attr-defined]

    return render(
        request,
        "users/public_profile.html",
        {
            "profile_user": profile_user,
            "articles": articles,
            "liked_articles": liked_articles,
        },
    )