from django.urls import path
from .views import accueil, article_id 
from .postViews import article_new

urlpatterns = [
    path('accueil', accueil, name='accueil'),
    path('article/<int:id>/', article_id, name = "article_id"),
    path('article/new/', article_new, name = "article_new")
]
