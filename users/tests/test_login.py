import pytest
from django.urls import reverse
from users.models import User

@pytest.mark.django_db
def test_login(client):
    username="Roberto"
    password="Test1234!"
    user= User.objects.create_user(username=username, password=password)
    url = reverse('login')
    data = {
        'username': username,
        'password': password
    }
    response = client.post(url, data=data, follow=False)

    # Vérifier la redirection vers 'accueil'
    assert response.status_code == 302
    assert response.url == reverse('accueil')

    # Vérifier que l'utilisateur est connecté
    assert client.session['_auth_user_id'] == str(user.id)