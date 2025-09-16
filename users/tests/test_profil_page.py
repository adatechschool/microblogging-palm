import pytest
from django.urls import reverse
from django.test import Client
from articles.models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_profile_page_userinfo():
      
      user = User.objects.create_user(
        username= 'testuser',
        email= 'test@example.com',
        first_name='test',
        last_name='testtest'
      )

      client = Client()
      client.force_login(user)
      url = reverse('profile')

      response = client.get(url, follow=False)

      assert response.status_code == 200
      assert response.context['user'] == user
      assert response.context['user'].username == 'testuser'
      assert response.context['user'].email == 'test@example.com'
      assert response.context['user'].first_name == 'test'
      assert response.context['user'].last_name == 'testtest'

  
@pytest.mark.django_db
def test_profile_page_posts():
      user = User.objects.create_user(
        username= 'testuser',
        email= 'test@example.com',
        first_name='test',
        last_name='testtest'
      )

      article = Article.objects.create(
            title="Mon premier post !",
            content="Ceci est mon premier post !",
            user=user
      )

      client = Client()
      client.force_login(user)
      url = reverse('profile')

      response = client.get(url, follow=False)

      assert response.status_code == 200

      assert 'articles' in response.context

      articles = response.context['articles']

      assert len(articles) == 1

      assert articles[0] == article
      assert articles[0].title == "Mon premier post !"
      assert articles[0].content == "Ceci est mon premier post !"
