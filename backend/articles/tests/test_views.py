import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from articles.models import Article

@pytest.mark.django_db
def test_get_posts_returns_list():
    Article.objects.create(title="Mon premier post", content="Hello world!", user_id=1)
    Article.objects.create(title="Mon 2e post", content="Hey world!", user_id=1)

    client = APIClient()
    url = reverse('accueil')
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['title'] == "Mon premier post"
    assert data[1]['title'] == "Mon 2e post"


@pytest.mark.django_db
def test_get_article_by_id():
    article = Article.objects.create(id=1, title="Mon premier post", content="Hello world!", user_id=2)

    client = APIClient()
    url = reverse('article_id', kwargs={"id":article.id})
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, object)
    assert len(data) == 6
    assert article.title == "Mon premier post"
        
