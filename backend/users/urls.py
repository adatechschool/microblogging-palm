from django.urls import path

from users.views.login_page import logout_user



urlpatterns = [

    path('logout/', logout_user, name='logout'),
    
]