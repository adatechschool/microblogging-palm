from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def accueil(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_id(request, id):
    articles = get_object_or_404(Article, id = id)
    serializer = ArticleSerializer(articles)
    return Response(serializer.data)