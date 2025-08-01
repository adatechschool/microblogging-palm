from django.urls import path
from .views import article_detail_html, accueil_html
from .postViews import article_new_html, delete_post, edit_post
from .likeViews import like
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accueil', accueil_html, name='accueil'),
    path('article/<int:id>/', article_detail_html, name = "article_detail_html"),
    path('article/newpost/', article_new_html, name = "article_new_html"),
    path('article/supprimer/<int:article_id>/', delete_post, name='delete_post'),
    path('article/modifier/<int:article_id>/', edit_post, name='edit_post'),
    path('article/<int:article_id>/like/', like, name='like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
