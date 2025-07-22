from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user_name
    
    # pour appliquer le nom exact de notre table, au lieu de la convention Django
    class Meta :
        db_table="users"  