from django.contrib import admin
from django.urls import path

from users.views.login_page import login_page, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
]