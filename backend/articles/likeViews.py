from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import get_object_or_404

@login_required
def like(request, article_id):
    article = get_object_or_404(Article, id = article_id)

    # Ne pas autoriser l'utilisateur à liker ses propres articles
    if article.user == request.user:
        return redirect('article_detail_html', id=article.id)

    if request.method == 'POST':
        if request.user in article.liked_by.all():
            article.liked_by.remove(request.user) 
        else:
            article.liked_by.add(request.user)

        return redirect('article_detail_html', id=article.id)



