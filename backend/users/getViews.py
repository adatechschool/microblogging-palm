from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404

#@api_view(['GET'])
#def accueil(request):
#    articles = Article.objects.all()
#    serializer = ArticleSerializer(articles, many=True)
#    return Response(serializer.data)


@api_view(['GET'])
def profil_id(request, id):
    user = get_object_or_404(User, id = id)
    serializer = UserSerializer(user)
    return Response(serializer.data)