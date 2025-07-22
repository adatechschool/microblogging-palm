import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from articles.models import Article

@pytest.mark.django_db
def test_get_posts_returns_list():
    Article.objects.create(title="Mon premier post", content="Hello world!", user_id=1)

    client = APIClient()
    url = reverse('accueil')
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['title'] == "Mon premier post"
