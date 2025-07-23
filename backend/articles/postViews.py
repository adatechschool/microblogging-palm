from rest_framework.decorators import api_view
from .models import Article
from django.shortcuts import render, redirect
import json
# @api_view(['POST'])
# def article_new(request):
#     if request.method == 'POST':
#       print(request.POST)
#       article_new = Article (
#           title = request.POST.get('title'),
#           content = request.POST.get('content'),
#           user_id = request.POST.get('user_id'),
#           created_at = request.POST.get('created_at'),
#           updated_at = request.POST.get('updated_at'),
#       )
#       print(request.POST)
#       article_new.save()
#       return redirect('/accueil')
#     else:
#       return render(request, 'newpost.html')
    


@api_view(['POST'])
def article_new(request):
    if request.method == 'POST':
      if request.content_type == 'application/json':
          data = json.loads(request.body)
          article = Article(
            title = data.get('title'),
            content = data.get('content'),
            user_id = data.get('user_id'),
            created_at = data.get('created_at'),
            updated_at = data.get('updated_at')
          )
          
      else:
          article = Article(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            user_id = request.POST.get('user_id'),
            created_at = request.POST.get('created_at'),
            updated_at = request.POST.get('updated_at')
          )
      article.save()
      return redirect('/accueil')
    return render(request, 'newpost.html')