"""
URL configuration for palmblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from palmblog.views import home
from articles.views import article_detail_html, accueil_html

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/', home, name='home'),
    path('accueil', accueil_html, name='accueil'),
    path('articles/', include('articles.urls')),  # inclut les routes de l'app articles
    path('users/', include('users.urls')), #peut-être à changer par profils/ ??
]