from django.urls import path
from .views import accueil, article_id
from .views import article_detail_html, accueil_html
from .postViews import article_new

urlpatterns = [
    path('accueil', accueil_html, name='accueil'),
    #path('article/<int:id>/', article_id, name = "article_id"),
    path('article/<int:id>/', article_detail_html, name = "article_detail_html"),
    path('article/new/', article_new, name = "article_new")
]
