import pytest
from django.contrib.auth import get_user_model
from articles.models import Article

User = get_user_model()

@pytest.fixture
def auteur(db):
    return User.objects.create_user(
        username='auteur',
        password='password123',
        email='auteur@example.fr'
    )

@pytest.fixture
def lecteur(db):
    return User.objects.create_user(
        username='lecteur',
        password='password1234',
        email='lecteur@example.fr'
    )

@pytest.fixture
def article(auteur):
    return Article.objects.create(
        title='Article de test',
        content='Contenu de test',
        user=auteur
    )
