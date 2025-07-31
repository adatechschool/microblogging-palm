# Palm MicroBlogging


## Stack technique

**Client:** Django Templates (HTML/CSS)

**Serveur:** Django


## Prérequis

Demander les variables d'environnement aux collaborateurs de ce projet pour créer votre .env à la racine du projet

Python 3.8+ installé

pip (gestionnaire de paquets Python)

virtualenv (recommandé pour isoler l'environnement)


## Installation

Clôner le dépôt git

```bash
git clone https://github.com/adatechschool/microblogging-palm
cd microblogging-palm
```

Créez et activez un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

Installez les dépendances
```bash
pip install -r requirements.txt
```

Configurez les variables d'environnement dans un fichier .env à la racine du projet

Copier Coller les variables d'environnement fournies par l'équipe qui a produit ce projet

Appliquez les migrations pour configurer la base de données
```bash
python manage.py migrate
```

Lancez le serveur de développement
```bash
python manage.py runserver
```

Accédez à l'application sur: http://127.0.0.1:8000/


## Fonctionnalitées

- Se connecter
- Se déconnecter
- Poster un article
- Consulter un article
- Like / Unlike un article
- Consulter son profil
- Consulter le profil des autres utilisateurs
- Modifier son profil
- Supprimer son compte


## Auteurs

- [@Pamela](https://github.com/Pampamlela)
- [@Auriane](https://github.com/aurianebgnl)
- [@Léo](https://github.com/LeoV0)
- [@Michel](https://github.com/Mlheriteau)
