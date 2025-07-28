import pytest
from django.urls import reverse
from users.models import User

@pytest.mark.django_db
def test_login(client):
    username="Roberto"
    password="Test1234!"
    user= User.objects.create_user(username=username, password=password)
    client.force_login(user)