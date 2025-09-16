import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_signup_page():
    client = Client()
    url = reverse('signup')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'TestPass123!',
        'password2': 'TestPass123!'
    }

    response = client.post(url, data=data, follow=False)

    if response.status_code != 302:
        if response.context and 'form' in response.context:
            print("Erreurs du formulaire :", response.context['form'].errors)
        assert False, f"La requête POST a renvoyé {response.status_code} au lieu de 302. Vérifiez les erreurs du formulaire."

    assert response.status_code == 302
    assert response.url == reverse('accueil')

    assert User.objects.filter(username='testuser').exists()
    user = User.objects.get(username='testuser')
    assert user.email == 'test@example.com'
    assert user.first_name == 'Test'
    assert user.last_name == 'User'
    assert user.check_password('TestPass123!')
    assert client.session.get('_auth_user_id') == str(user.id)  # Vérifier que l'utilisateur est connecté