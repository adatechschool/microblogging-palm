import os
import django
import random
from pathlib import Path
from django.core.files.uploadedfile import SimpleUploadedFile

# Initialise Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "palmblog.settings")
django.setup()

from users.models import User
from articles.models import Article
from django.utils import timezone

# Nettoyage (facultatif)
User.objects.all().delete()
Article.objects.all().delete()

# Image factice par défaut
dummy_image_path = Path(__file__).parent / "default.jpg"
if not dummy_image_path.exists():
    # Crée une image vide si elle n'existe pas encore
    with open(dummy_image_path, "wb") as f:
        f.write(b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4C\x01\x00\x3B")

# Utilisateurs à créer
users_data = [
    {"username": "alice", "email": "alice@example.com", "password": "S3cret!s"},
    {"username": "bob", "email": "bob@example.com", "password": "S3cret!s"},
    {"username": "charlie", "email": "charlie@example.com", "password": "S3cret!s"},
]

users = []
for data in users_data:
    user = User.objects.create_user(
        username=data["username"],
        email=data["email"],
        password=data["password"],
    )
    # Ajoute une image par défaut
    with open(dummy_image_path, "rb") as img_file:
        user.profile_photo.save("default.jpg", SimpleUploadedFile("default.jpg", img_file.read(), content_type="image/jpeg"))
    users.append(user)

print("✅ Utilisateurs créés avec photo de profil.")

# Titres et contenus d'articles
titles = [
    "Introduction à Django",
    "Comment fonctionne le modèle MVC",
    "Créer une API REST avec Django",
    "Utilisation des formulaires Django",
    "Gérer les fichiers statiques",
    "Déploiement d'une app Django sur Heroku"
]

# Création d’articles aléatoires
for user in users:
    for _ in range(random.randint(3, 4)):
        title = random.choice(titles)
        content = f"Ceci est un article généré automatiquement : {title}."
        Article.objects.create(
            title=title,
            content=content,
            user=user,
            created_at=timezone.now()
        )

print("Articles créés pour chaque utilisateur.")