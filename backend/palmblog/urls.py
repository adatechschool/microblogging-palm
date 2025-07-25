from django.contrib import admin
from django.urls import path, include

from palmblog.views import home
from users.views.login_page import login_page, logout_user
from users.views.signup_page import signup_page
from users.views import profile_page, edit_profile, delete_profile, public_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('inscription/', signup_page, name='signup'),
    path('accueil/', home, name='home'),
    path('article/', include('articles.urls')),  # inclut les routes de l'app articles
    path('users/', include('users.urls')), #peut-être à supprimer ?
    path('monprofil/', profile_page.profile_view, name='profile'),
    path('monprofil/modifier/', edit_profile.edit_profile_view, name='edit_profile'),
    path('monprofil/supprimer/', delete_profile.delete_profile_view, name='delete_profile'),
    path('profil/<int:user_id>/', public_profile.public_profile_view, name='public_profile'),
]