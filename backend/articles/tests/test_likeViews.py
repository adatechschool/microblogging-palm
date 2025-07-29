import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from articles.models import Article


@pytest.mark.django_db
def test_user_cannot_like_own_article(client, article, auteur):
    client.login(username='auteur', password='password123')

    # Tentative de like
    url = reverse('like', args=[article.id])
    response = client.post(url)

    # Vérifier que le like n'a pas été ajouté
    assert auteur not in article.liked_by.all()

    # Vérifier la redirection
    assert response.status_code == 302
    assert response.url == reverse('article_detail_html', args=[article.id])


@pytest.mark.django_db
def test_user_can_like_others_article(client, article, lecteur):
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
def test_user_can_unlike_article(client, article, lecteur):
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
def test_redirect_after_like(client, article, lecteur):
    article.liked_by.add(lecteur)

    client.login(username='lecteur', password='password1234')

    url = reverse('like', args=[article.id])
    response = client.post(url)
    
    assert response.status_code == 302
    assert response.url == reverse('article_detail_html', args=[article.id])