from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_id = models.BigIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
