# MangaCollec API

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/poetry-dependency%20management-blue.svg)](https://python-poetry.org/)
[![Version](https://img.shields.io/badge/version-0.1.78-green.svg)](https://github.com/shooter-dev/mangacollec_api)

Une bibliothèque Python pour interagir avec l'API MangaCollec, permettant de récupérer des informations sur les mangas, séries, auteurs, éditeurs et plus encore.

## Table des matières

- [Installation](#installation)
- [Configuration](#configuration)
- [Authentification](#authentification)
- [Utilisation rapide](#utilisation-rapide)
- [Endpoints disponibles](#endpoints-disponibles)
- [Entités](#entités)
- [Gestion des erreurs](#gestion-des-erreurs)
- [Architecture](#architecture)
- [Développement](#développement)
- [Licence](#licence)

## Installation

### Avec Poetry (recommandé)

```bash
poetry add mangacollec_api
```

### Avec pip

```bash
pip install mangacollec_api
```

## Configuration

### Variables d'environnement

Créez un fichier `.env` ou définissez les variables d'environnement suivantes :

```bash
# Obligatoire
CLIENT_ID=votre_client_id
CLIENT_SECRET=votre_client_secret

# Optionnel (pour l'authentification utilisateur)
USERNAME_DEV=votre_email@example.com
PASSWORD=votre_mot_de_passe
```

## Authentification

L'API MangaCollec supporte deux modes d'authentification OAuth2 :

### 1. Authentification anonyme (client_credentials)

```python
from mangacollec_api.client import MangaCollecAPIClient

client = MangaCollecAPIClient(
    client_id="votre_client_id",
    client_secret="votre_client_secret"
)
```

### 2. Authentification utilisateur (password)

```python
from mangacollec_api.client import MangaCollecAPIClient

client = MangaCollecAPIClient(
    client_id="votre_client_id",
    client_secret="votre_client_secret",
    email="votre_email@example.com",
    password="votre_mot_de_passe"
)
```

### 3. Avec proxy (optionnel)

```python
client = MangaCollecAPIClient(
    client_id="votre_client_id",
    client_secret="votre_client_secret",
    proxy={
        "http": "http://proxy-server:port",
        "https": "https://proxy-server:port"
    }
)
```

## Utilisation rapide

### Récupérer toutes les séries

```python
import os
from mangacollec_api.client import MangaCollecAPIClient
from mangacollec_api.serie.endpoint.serie_endpoint import SerieEndpoint

# Initialisation du client
client = MangaCollecAPIClient(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET")
)

# Endpoint des séries
serie_endpoint = SerieEndpoint(client)

# Récupérer toutes les séries (API v2)
series = serie_endpoint.get_all_series_v2()
print(f"Nombre de séries : {len(series)}")

for serie in series[:5]:  # Afficher les 5 premières
    print(f"- {serie.title} (ID: {serie.id})")
```

### Récupérer une série spécifique

```python
# Récupérer une série par son ID avec toutes les informations associées
serie_id = "a320ac19-4318-4471-9e4e-eb017f4584d5"
serie_complete = serie_endpoint.get_series_by_id_v2(serie_id)

# Informations de base
serie = serie_complete.serie
print(f"Titre: {serie.title}")
print(f"Contenu adulte: {serie.adult_content}")
print(f"Nombre d'éditions: {serie.editions_count}")

# Informations associées
print(f"Genres: {[kind.name for kind in serie_complete.kinds]}")
print(f"Auteurs: {[author.name for author in serie_complete.authors]}")
print(f"Éditeurs: {[pub.name for pub in serie_complete.publishers]}")
```

## Endpoints disponibles

La bibliothèque propose plusieurs endpoints pour interagir avec l'API :

### SerieEndpoint
- `get_all_series()` - Récupère toutes les séries (API v1)
- `get_all_series_v2()` - Récupère toutes les séries (API v2)
- `get_series_by_id(series_id)` - Récupère une série par ID (API v1)
- `get_series_by_id_v2(series_id)` - Récupère une série complète par ID (API v2)

### Autres endpoints disponibles
- `AuthorEndpoint` - Gestion des auteurs
- `EditionEndpoint` - Gestion des éditions
- `GenreEndpoint` - Gestion des genres
- `JobEndpoint` - Gestion des métiers
- `KindEndpoint` - Gestion des types
- `PublisherEndpoint` - Gestion des éditeurs
- `UserEndpoint` - Gestion des utilisateurs
- `VolumeEndpoint` - Gestion des volumes

## Entités

### Serie
```python
class Serie:
    id: str                    # Identifiant unique
    title: str                 # Titre de la série
    type_id: str              # ID du type/genre
    adult_content: bool       # Contenu adulte
    editions_count: int       # Nombre d'éditions
    tasks_count: int          # Nombre de tâches
    kinds_ids: List[str]      # IDs des types associés
```

### Autres entités disponibles
- `Author` - Informations sur les auteurs
- `Edition` - Détails des éditions
- `Volume` - Informations sur les volumes
- `Publisher` - Données des éditeurs
- `Genre` - Types et genres
- `Box` - Informations sur les coffrets
- `Task` - Tâches associées

## Gestion des erreurs

La bibliothèque définit plusieurs exceptions personnalisées :

```python
from mangacollec_api.exceptions import (
    MangaCollecAPIError,
    AuthenticationError,
    AuthorizationError,
    NotFoundError,
    BadRequestError,
    ServerError,
    RateLimitExceededError
)

try:
    serie = serie_endpoint.get_series_by_id_v2("invalid-id")
except NotFoundError:
    print("Série non trouvée")
except AuthenticationError:
    print("Erreur d'authentification")
except MangaCollecAPIError as e:
    print(f"Erreur API: {e}")
```

## Architecture

Le projet suit une architecture modulaire avec des interfaces :

```
src/mangacollec_api/
├── client.py              # Client principal API
├── auth.py               # Gestion authentification OAuth2
├── exceptions.py         # Exceptions personnalisées
├── endpoints/            # Endpoints API
│   ├── serie_endpoint.py
│   ├── author_endpoint.py
│   └── ...
├── entity/              # Modèles de données
│   ├── serie.py
│   ├── author.py
│   └── ...
└── interfaces/          # Interfaces abstraites
    ├── auth/
    ├── client/
    └── endpoints/
```

### Fonctionnalités clés

- **Authentification automatique** : Gestion transparente des tokens OAuth2
- **Refresh automatique** : Renouvellement automatique des tokens expirés
- **Support multi-version** : API v1 et v2 supportées
- **Gestion d'erreurs** : Exceptions spécifiques pour chaque type d'erreur
- **Architecture modulaire** : Interfaces pour faciliter les tests et l'extension
- **Support proxy** : Configuration proxy pour les environnements d'entreprise

## Développement

### Installation pour le développement

```bash
git clone https://github.com/shooter-dev/mangacollec_api.git
cd mangacollec_api
poetry install
```

### Lancer les tests

```bash
poetry run pytest
```

### Structure des tests

```
tests/
├── endpoints/
│   ├── test_series.py
│   └── test_volumes.py
└── ...
```

### Contribuer

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Créez une Pull Request

## Dépendances

- **Python** : 3.10+
- **requests** : ^2.32.3

### Dépendances de développement
- **pytest** : ^8.3.5
- **pytest-mock** : ^3.14.0
- **requests-mock** : ^1.12.1

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Contact

- **Auteur** : shooter-dev
- **Email** : vincentbleach@gmail.com
- **Repository** : [https://github.com/shooter-dev/mangacollec_api](https://github.com/shooter-dev/mangacollec_api)

---

## Exemple complet

```python
import os
from mangacollec_api.client import MangaCollecAPIClient
from mangacollec_api.serie.endpoint.serie_endpoint import SerieEndpoint

def main():
    # Configuration du client
    client = MangaCollecAPIClient(
        client_id=os.environ.get("CLIENT_ID"),
        client_secret=os.environ.get("CLIENT_SECRET"),
        # Optionnel pour l'authentification utilisateur
        email=os.environ.get("USERNAME_DEV"),
        password=os.environ.get("PASSWORD")
    )
    
    # Initialisation de l'endpoint
    serie_endpoint = SerieEndpoint(client)
    
    # Récupération des données
    try:
        # Liste des séries
        series = serie_endpoint.get_all_series_v2()
        print(f"Total des séries : {len(series)}")
        
        # Détail d'une série
        if series:
            serie_detail = serie_endpoint.get_series_by_id_v2(series[0].id)
            print(f"Série : {serie_detail.serie.title}")
            print(f"Auteurs : {[a.name for a in serie_detail.authors]}")
            
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
