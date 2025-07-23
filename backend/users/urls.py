from django.urls import path
from .views import profil_id 


urlpatterns = [
    path('profil/<int:id>/', profil_id, name = "profil_id"),
]
