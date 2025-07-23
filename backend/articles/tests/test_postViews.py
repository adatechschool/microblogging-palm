import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from articles.models import Article

@pytest.mark.django_db
def test_post_article():
    # article = Article.objects.create(title="Mon premier post", content="Hello world!", user_id=2)
    json_data = {
          "title": "Nouveau post",
          "content": "Léo est très très content",
          "user_id": 1
    }

    client = APIClient()
    url = reverse('article_new')
    response = client.post(url, data=json_data, format='json')

    assert response.status_code == 201

    response_data = response.json()
    assert 'message' in response_data
    assert response_data['message'] == 'Article créé avec succès'
    assert 'id' in response_data

    article = Article.objects.get(id=response_data['id'])
    assert article.title == json_data['title']
    assert article.content == json_data['content']
    assert article.user_id == json_data['user_id']

@pytest.mark.django_db
def test_post_article_missing_fields():
    # Données avec un champ manquant
    json_data = {
        "title": "Nouveau post",
        "user_id": 1
        # 'content' est manquant
    }

    client = APIClient()
    url = reverse('article_new')

    # Envoyer une requête POST avec JSON
    response = client.post(url, data=json_data, format='json')

    # Vérifier que la requête échoue avec un code 400
    assert response.status_code == 400

    # Vérifier le message d'erreur
    response_data = response.json()
    assert 'error' in response_data
    assert response_data['error'] == 'Tous les champs (title, content, user_id) sont requis'

@pytest.mark.django_db
def test_post_article_invalid_json():
    client = APIClient()
    url = reverse('article_new')

    # Envoyer une requête POST avec JSON invalide
    response = client.post(url, data="invalid json", content_type='application/json')

    # Vérifier que la requête échoue avec un code 400
    assert response.status_code == 400

    # Vérifier le message d'erreur
    response_data = response.json()
    assert 'error' in response_data
    assert response_data['error'] == 'JSON invalide'