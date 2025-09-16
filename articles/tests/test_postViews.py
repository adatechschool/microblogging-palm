import pytest
from django.urls import reverse
from django.test import Client
from articles.models import Article
from users.models import User

@pytest.mark.django_db
def test_post_article():
    user = User.objects.create_user(
        username="newuser",
        email="newuser@gmail.com",
        password="TestPass123!"
    )

    client = Client()
    client.force_login(user)

    url = reverse('article_new_html')

    data = {
    'title': 'mon titre',
    'content': 'mon contenu'
    }

    response = client.post(url, data=data, follow=False)

    assert response.status_code == 302
    assert response.url == reverse('accueil')

@pytest.mark.django_db
def test_post_article_missing_fields():
    # Données avec un champ manquant !!
    user = User.objects.create_user(
        username="newuser",
        email="newuser@gmail.com",
        password="TestPass123!"
    )

    data = {
    'title': 'mon titre',
    # 'content': 'mon contenu' champs manquant
    }

    client = Client()
    client.force_login(user)

    url = reverse('article_new_html')

    # Envoyer une requête POST avec JSON
    response = client.post(url, data="invalid json", content_type='application/json')

    assert response.status_code == 200  # La vue rend newpost.html
    assert 'error' in response.context
    assert response.context['error'] == 'Tous les champs sont requis.'
    assert not Article.objects.filter(title='mon titre').exists()



@pytest.mark.django_db
def test_post_article_invalid_json():
    user = User.objects.create_user(
        username="newuser",
        email="newuser@gmail.com",
        password="TestPass123!"
    )
    
    client = Client()
    client.force_login(user)
    url = reverse('article_new_html')

    response = client.post(url, data="invalid json", content_type='application/json')

    assert response.status_code == 200
    assert 'error' in response.context
    assert response.context['error'] == 'Tous les champs sont requis.'
    assert not Article.objects.filter(title='mon titre').exists()