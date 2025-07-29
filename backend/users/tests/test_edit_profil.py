import pytest
from django.urls import reverse
from django.test import Client
from users.models import User


@pytest.mark.django_db
def test_edit_profil():
    client = Client()
    url = reverse('edit_profile')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        # 'profile_photo': ''
    }
    response = client.post(url, data=data)

    assert response.status_code == 302
    assert response.url == reverse('profile')
    assert User.objects.filter(username='testuser').exists()
    user = User.objects.get(username='testuser')
    assert user.email == 'test@example.com'