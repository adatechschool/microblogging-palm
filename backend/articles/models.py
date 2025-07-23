from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_id = models.BigIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    # pour appliquer le nom exact de notre table, au lieu de la convention Django
    class Meta :
        db_table="articles"
