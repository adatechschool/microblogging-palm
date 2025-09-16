from django.db import models
from django.conf import settings

class Article (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles') # nom personnalisé
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_articles')  # nom différent

    def __str__(self):
        return self.title
    
    # pour appliquer le nom exact de notre table, au lieu de la convention Django
    class Meta :
        db_table="articles"
        ordering = ('-created_at',) #pour avoir un tri par défaut de nos articles
                                    # la , est importante !
