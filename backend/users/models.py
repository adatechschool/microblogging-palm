from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

    email = models.EmailField(unique=True)
   
    profile_photo = models.ImageField(
        verbose_name='Photo de profil',
        # upload_to='profile_photos/',   # <- important pour stocker dans un dossier propre
        # blank=True,
        # null=True
        )

    # pour appliquer le nom exact de notre table, au lieu de la convention Django
    class Meta :
        db_table="users" 