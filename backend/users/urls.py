from django.urls import path
from .updatedViews import user_update

urlpatterns = [
    path('profil/<int:id>/', user_update, name = "user_update"),
]
