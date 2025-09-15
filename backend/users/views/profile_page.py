from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from articles.models import Article
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseNotAllowed,
)

# @login_required
# def profile_view(request):
#     user = request.user
#     articles = Article.objects.filter(user=user).order_by('-created_at')    

#     return render(request, 'users/profile.html', {
#         'user': request.user,
#         'articles': articles,
#     })

@login_required
def profile(request):
    user = request.user
    articles = Article.objects.filter(user=user).order_by('-created_at')
    user_articles = user.articles.all() # type: ignore[attr-defined]
    liked_articles = user.liked_articles.all() # type: ignore[attr-defined]

    return render(
        request,
        "users/profile.html",
        {
            "user": user,
            "articles": articles,
            "user_articles": user_articles,
            "liked_articles": liked_articles,
        },
    )