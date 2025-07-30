from django import forms
from .models import User

AVATAR_CHOICES = [
    ('avatar1.png', 'Avatar 1'),
    ('avatar2.png', 'Avatar 2'),
    ('avatar3.png', 'Avatar 3'),
    ('avatar4.png', 'Avatar 4'),
    ('avatar5.png', 'Avatar 5'),
]

class AvatarChoiceForm(forms.ModelForm):
    avatar_choice = forms.ChoiceField(
        choices=AVATAR_CHOICES,
        widget=forms.RadioSelect,
        label="Choisis ton avatar"
    )

    class Meta:
        model = User
        fields = ['avatar_choice']