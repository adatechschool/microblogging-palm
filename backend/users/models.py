from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

    email = models.EmailField(unique=True)
   

    avatar_choice = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Nom du fichier avatar choisi parmi les prédéfinis"
    )

    # pour appliquer le nom exact de notre table, au lieu de la convention Django
    class Meta :
        db_table="users" 
