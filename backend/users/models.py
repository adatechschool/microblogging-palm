from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_name
    
    # pour appliquer le nom exact de notre table, au lieu de la convention Django
    class Meta :
        db_table="users"  