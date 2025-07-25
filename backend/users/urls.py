from django.contrib import admin
from django.urls import path

from users.views.login_page import login_page, logout_user
from users.views.signup_page import signup_page
# from users.views.profile_page import profile_view
from .views import profile_page, edit_profile, delete_profile 


urlpatterns = [
    path('', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_page, name='signup'),
    path('profile/', profile_page.profile_view, name='profile'),
    path('profile/edit/', edit_profile.edit_profile_view, name='edit_profile'),
    path('profile/delete/', delete_profile.delete_profile_view, name='delete_profile'),
]