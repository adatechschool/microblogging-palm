from django.urls import path
from .views import accueil, article_id
from .views import article_detail_html, accueil_html
from .postViews import article_new_html, test_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accueil', accueil_html, name='accueil'),
    #path('article/<int:id>/', article_id, name = "article_id"),
    path('article/<int:id>/', article_detail_html, name = "article_detail_html"),
    path('article/newpost/', article_new_html, name = "article_new_html"),
    path('article/test/', test_view, name = "test_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
