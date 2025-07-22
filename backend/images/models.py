from django.db import models

# Create your models here.
class Image(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.description
    
    # pour appliquer le nom exact de notre table, au lieu de la convention Django
    class Meta :
        db_table="images"