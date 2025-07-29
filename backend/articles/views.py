from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def accueil(request):
    articles = Article.objects.all()
    #if request.headers.get('Accept') == 'application/json':
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
    #return render(request, 'accueil.html', {'articles': articles})

@api_view(['GET'])
def article_id(request, id):
    articles = get_object_or_404(Article, id = id)
    serializer = ArticleSerializer(articles)
    return Response(serializer.data)

def accueil_html(request):
    articles=Article.objects.all() #.order_by('-created_at') #pour trier les articles du plus récent au plus vieux grace au '-' devant la valeur
    article_ids=[article.id for article in articles]
    request.session["articles_affiches"]=article_ids
    return render(request, 'accueil.html', {'articles': articles})

def article_detail_html(request, id):
    articles_affiches=request.session.get("articles_affiches",[])
    if id not in articles_affiches:
        return render(request,"non_autorise.html", status=403)
    article=get_object_or_404(Article, id = id)
    return render(request,"article_detail.html",{"article":article})