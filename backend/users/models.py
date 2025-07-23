from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

    email = models.EmailField(unique=True)
    # username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    profile_photo = models.ImageField(verbose_name='Photo de profil')

    # pour appliquer le nom exact de notre table, au lieu de la convention Django
    class Meta :
        db_table="users"  

    # user_name = models.CharField(max_length=255)
    # birthdate = models.DateField()
    # email = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    # created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)

    # def __str__(self):
    #     return self.user_name
    
  