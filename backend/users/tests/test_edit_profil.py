import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_edit_profil():
    user = User.objects.create_user(
        username="olduser",
        email="old@gmail.com",
        first_name="test",
        last_name="test",
        password="Test1234!"
    )

    client = Client()
    client.force_login(user)

    url = reverse('edit_profile')
    response_get = client.get(url)
    form = response_get.context['form']
    avatar_choices = form.fields['avatar_choice'].choices
    valid_avatar = avatar_choices[1][0]  # sauter le choix vide s'il existe

    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'first_name': 'test',
        'last_name': 'test',
        'avatar_choice': valid_avatar
    }

    data['csrfmiddlewaretoken'] = client.cookies.get('csrftoken').value
    response = client.post(url, data=data, follow=False)

    if response.status_code != 302:
        form = response.context.get('form')
        if form:
            print("Form errors:", form.errors)

    assert response.status_code == 302
    assert response.url == reverse('profile')
    assert User.objects.filter(username='testuser').exists()
    user = User.objects.get(username='testuser')
    assert user.email == 'test@example.com'
    assert user.first_name == 'test'
    assert user.last_name == 'test'
