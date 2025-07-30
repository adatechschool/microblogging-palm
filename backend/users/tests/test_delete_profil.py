import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_delete_profile():
      user = User.objects.create_user(
        username= 'testuser',
        email= 'test@example.com',
        password= 'TestPass123!'
      )

      client = Client()
      client.force_login(user)
      url = reverse("delete_profile")
      response = client.post(url, follow=False)

      assert response.status_code == 302
      assert response.url == reverse('home')
      assert not User.objects.filter(username='testuser').exists()
      assert '_auth_user_id' not in client.session