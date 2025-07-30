import pytest
from django.urls import reverse
from django.test import Client
from articles.models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_get_posts_returns_list():
    user = User.objects.create_user(
        username="newuser",
        email="newuser@gmail.com",
        password="TestPass123!"
    )
    Article.objects.create(
        title="Mon premier post",
        content="Hello world!",
        user=user
    )

    client = Client()
    client.force_login(user)
    url = reverse('accueil')
    response = client.get(url, follow=False)

    assert response.status_code == 200
    assert 'page_obj' in response.context
    articles = response.context['page_obj']
    assert len(articles) == 1
    assert articles[0].title == "Mon premier post"
    assert articles[0].content == "Hello world!"
    assert articles[0].user.id == user.id


@pytest.mark.django_db
def test_get_article_by_id():
    user = User.objects.create_user(
        username="newuser",
        email="newuser@gmail.com",
        password="TestPass123!"
    )
    article = Article.objects.create(
        title="Mon premier post",
        content="Hello world!",
        user=user
    )

    client = Client()
    client.force_login(user)
    # Appeler accueil_html pour initialiser la session
    accueil_url = reverse('accueil')
    client.get(accueil_url, follow=False)  # Cela définit articles_affiches dans la session
    url = reverse('article_detail_html', kwargs={"id": article.id})
    response = client.get(url, follow=False)

    assert response.status_code == 200
    assert 'article' in response.context
    article_data = response.context['article']
    assert article_data.title == "Mon premier post"
    assert article_data.content == "Hello world!"
    assert article_data.user.id == user.id