from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from articles.models import Article

@login_required
def profile_view(request):
    user = request.user
    articles = Article.objects.filter(user=user).order_by('-created_at')
    #articles = request.user.articles.all()    

    return render(request, 'users/profile.html', {
        'user': request.user,
        'articles': articles,
    })
 