import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from articles.models import Article

User = get_user_model()   #Django ne permet pas d’utiliser auth.User quand il a été remplacé par un modèle custom.


@pytest.mark.django_db
def test_user_cannot_like_own_article(client):
    # Créer un utilisateur et se connecter avec fixture client
    auteur = User.objects.create_user(username='auteur', password='password123')
    client.login(username='auteur', password='password123')

    # Créer un article appartenant à cet utilisateur
    article = Article.objects.create(
        title='Article de test',
        content='Contenu de test',
        user=auteur
    )

    # Tentative de like
    url = reverse('like', args=[article.id])
    response = client.post(url)

    # Vérifier que le like n'a pas été ajouté
    assert auteur not in article.liked_by.all()

    # Vérifier la redirection
    assert response.status_code == 302
    assert response.url == reverse('article_detail_html', args=[article.id])


@pytest.mark.django_db
def test_user_can_like_others_article(client):
    # Créer un utilisateur et se connecter avec fixture client
    auteur = User.objects.create_user(username='auteur', password='password123', email='auteur@example.fr')
    
    article = Article.objects.create(
        title='Article de test',
        content='Contenu de test',
        user=auteur
    )

    lecteur = User.objects.create_user(username='lecteur', password='password1234', email='lecteur@example.fr')
    client.login(username='lecteur', password='password1234')

    # Tentative de like
    url = reverse('like', args=[article.id])
    response = client.post(url)

    # Rafraîchir les données depuis la base
    article.refresh_from_db()

    assert lecteur in article.liked_by.all()

    assert response.status_code == 302
    assert response.url == reverse('article_detail_html', args=[article.id])


@pytest.mark.django_db
def test_user_can_unlike_article(client):
    auteur = User.objects.create_user(username='auteur', password='password123', email='auteur@example.fr')
    
    article = Article.objects.create(
        title='Article de test',
        content='Contenu de test',
        user=auteur
    )

    lecteur = User.objects.create_user(username='lecteur', password='password1234', email='lecteur@example.fr')
    article.liked_by.add(lecteur)

    client.login(username='lecteur', password='password1234')

    # Tentative de unlike
    url = reverse('like', args=[article.id])
    response = client.post(url)

    # Rafraîchir les données depuis la base
    article.refresh_from_db()

    assert lecteur not in article.liked_by.all()

    assert response.status_code == 302
    assert response.url == reverse('article_detail_html', args=[article.id])

@pytest.mark.django_db
def test_redirect_after_like(client):
    auteur = User.objects.create_user(username='auteur', password='password123', email='auteur@example.fr')
    
    article = Article.objects.create(
        title='Article de test',
        content='Contenu de test',
        user=auteur
    )

    lecteur = User.objects.create_user(username='lecteur', password='password1234', email='lecteur@example.fr')
    article.liked_by.add(lecteur)

    client.login(username='lecteur', password='password1234')

    url = reverse('like', args=[article.id])
    response = client.post(url)
    
    assert response.status_code == 302
    assert response.url == reverse('article_detail_html', args=[article.id])