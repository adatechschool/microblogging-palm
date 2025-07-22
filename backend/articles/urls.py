from django.urls import path
from .views import accueil, article_id

urlpatterns = [
    path('accueil', accueil, name='accueil'),
    path('article/<int:id>/', article_id, name = "article_id")
]
