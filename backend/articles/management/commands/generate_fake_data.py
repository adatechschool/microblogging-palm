from django.core.management.base import BaseCommand
from faker import Faker
from articles.models import Article
from users.models import User
import random

fake = Faker('fr_FR')

class Command(BaseCommand):
    help = "Génère des utilisateurs, articles et likes fictifs"

    def handle(self, *args, **kwargs):
        self.stdout.write("Création de 5 utilisateurs fictifs...")

        # Création des utilisateurs
        users = []
        for _ in range(5):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="test1234"
            )
            users.append(user)
            self.stdout.write(f"Utilisateur créé: {user.username}")

        # Création des articles + likes
        for user in users:
            self.stdout.write(f"Création de 5 articles pour {user.username}...")
            for _ in range(5):
                article = Article.objects.create(
                    title=fake.sentence(nb_words=6),
                    content=fake.paragraph(nb_sentences=10),
                    user=user
                )
                # Choix aléatoire d'autres utilisateurs pour liker
                potential_likers = [u for u in users if u != user]
                likers = random.sample(potential_likers, k=random.randint(0, min(3, len(potential_likers))))

                for liker in likers:
                    article.liked_by.add(liker)

                self.stdout.write(f"- Article: {article.title} (likes: {len(likers)})")

        self.stdout.write(self.style.SUCCESS("✅ Données fictives générées avec succès."))
