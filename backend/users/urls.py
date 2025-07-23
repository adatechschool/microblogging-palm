from django.urls import path
from .views import delete_profile

urlpatterns = [
    path('delete-profile/<int:user_id>/', delete_profile, name='delete_profile'),
]