from .settings import *

SECRET_KEY = "fake-key-for-testing"

# Utilise SQLite en mémoire pour les tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}