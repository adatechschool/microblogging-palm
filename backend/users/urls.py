from django.contrib import admin
from django.urls import path

from users.views.login_page import login_page, logout_user
from users.views.signup_page import signup_page
from users.views.profile_page import profile_view

urlpatterns = [
    path('', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_page, name='signup'),
    path('profile/', profile_view, name='profile'),
]