from django.contrib import admin
from django.urls import path

from users.views.login_page import login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
]