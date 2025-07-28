from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from django.conf import settings

class Article (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # pour appliquer le nom exact de notre table, au lieu de la convention Django
    class Meta :
        db_table="articles"


#class Article(models.Model):
#    title = models.CharField(max_length=255)
#    content = models.TextField()
#    user = models.ForeignKey(
#        settings.AUTH_USER_MODEL,
#        on_delete=models.CASCADE,
#        related_name='articles')  # permet d’écrire user.articles.all())
#    created_at = models.DateTimeField(default=timezone.now)
#    updated_at = models.DateTimeField(default=timezone.now)
