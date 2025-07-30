import pytest
from django.urls import reverse
from django.test import Client
from users.models import User


@pytest.mark.django_db
def test_edit_profil():
    user = User.objects.create_user(
        username="olduser",
        email="old@gmail.com",
        password="TestPass123!"
    )

    client = Client()
    client.force_login(user)

    url = reverse('edit_profile')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        # 'profile_photo': ''
    }

    response = client.post(url, data=data, follow=False)

    assert response.status_code == 302
    assert response.url == reverse('profile')
    assert User.objects.filter(username='testuser').exists()
    user = User.objects.get(username='testuser')
    assert user.email == 'test@example.com'