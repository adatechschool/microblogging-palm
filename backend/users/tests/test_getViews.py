import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User

@pytest.mark.django_db
def test_get_profil_by_id():
    profil = User.objects.create(username="Pampamlela", email="pampamlela@gmail.com", password="1234")

    client = APIClient()
    url = reverse('profil_id', kwargs={"id":profil.id})
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, object)
    assert len(data) == 11
    assert profil.email == "pampamlela@gmail.com"