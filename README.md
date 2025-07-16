# MangaCollec API Client

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/poetry-dependency%20management-blue.svg)](https://python-poetry.org/)
[![Version](https://img.shields.io/badge/version-0.1.78-green.svg)](https://github.com/shooter-dev/mangacollec_api)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/shooter-dev/mangacollec_api)
[![Architecture](https://img.shields.io/badge/architecture-DDD-orange.svg)](https://github.com/shooter-dev/mangacollec_api)

Une bibliothèque Python moderne pour interagir avec l'API MangaCollec, suivant les principes du Domain-Driven Design (DDD) avec une architecture modulaire et une couverture de tests complète.

## 🎯 Fonctionnalités

- **🔐 Authentification OAuth2** - Support `client_credentials` et `password` grant types
- **🏗️ Architecture DDD** - Domain-Driven Design avec séparation claire des responsabilités
- **🔄 Multi-version API** - Support des endpoints v1 (legacy) et v2 (typés)
- **🔧 Interface-based Design** - Interfaces pour une meilleure testabilité et extensibilité
- **⚡ Gestion automatique** - Refresh de tokens et gestion d'erreurs transparente
- **🧪 Tests complets** - Couverture de tests optimisée avec pytest
- **🌐 Support proxy** - Configuration proxy pour environnements d'entreprise

## 📋 Table des matières

- [Installation](#installation)
- [Configuration rapide](#configuration-rapide)
- [Architecture](#architecture)
- [Authentification](#authentification)
- [Utilisation](#utilisation)
- [Domaines disponibles](#domaines-disponibles)
- [Tests](#tests)
- [Développement](#développement)
- [API Reference](#api-reference)
- [Contribution](#contribution)

## 🚀 Installation

### Avec Poetry (recommandé)

```bash
poetry add mangacollec_api
```

### Avec pip

```bash
pip install mangacollec_api
```

## ⚙️ Configuration rapide

### Variables d'environnement

```bash
# Obligatoire
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret

# Optionnel (authentification utilisateur)
USERNAME_DEV=your_email@example.com
PASSWORD=your_password
```

### Utilisation basique

```python
import os
from mangacollec_api.client.client import MangaCollecAPIClient
from mangacollec_api.serie.endpoint.serie_endpoint import SerieEndpoint

# Client anonyme
client = MangaCollecAPIClient(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET")
)

# Endpoint des séries
serie_endpoint = SerieEndpoint(client)

# Récupérer toutes les séries (API v2)
series = serie_endpoint.get_all_series_v2()
print(f"Nombre de séries : {len(series)}")
```

## 🏛️ Architecture

Ce projet suit une **architecture Domain-Driven Design (DDD)** avec une séparation claire des responsabilités :

### Structure générale

```
src/mangacollec_api/
├── core/                     # Infrastructure centrale
│   ├── exception/           # Exceptions de base
│   └── interfaces/          # Interfaces centralisées
├── client/                  # Client API et authentification
├── auth/                    # Gestion OAuth2
└── {domain}/               # Domaines métier (serie, author, etc.)
    ├── endpoint/           # Points d'accès API
    ├── entity/             # Entités métier
    ├── converter/          # Transformation de données
    ├── exception/          # Exceptions spécifiques
    └── tests/              # Tests unitaires du domaine
```

### Domaines disponibles

Chaque domaine suit la même structure modulaire :

- **author/** - Gestion des auteurs
- **serie/** - Gestion des séries
- **genre/** - Gestion des genres (type)
- **edition/** - Gestion des éditions
- **volume/** - Gestion des volumes
- **publisher/** - Gestion des éditeurs
- **job/** - Gestion des métiers
- **kind/** - Gestion des types
- **users/** - Gestion des utilisateurs
- **box/** - Gestion des coffrets
- **task/** - Gestion des tâches

## 🔐 Authentification

### Authentification anonyme (client_credentials)

```python
from mangacollec_api.client.client import MangaCollecAPIClient

client = MangaCollecAPIClient(
    client_id="your_client_id",
    client_secret="your_client_secret"
)
```

### Authentification utilisateur (password)

```python
client = MangaCollecAPIClient(
    client_id="your_client_id",
    client_secret="your_client_secret",
    email="your_email@example.com",
    password="your_password"
)
```

### Avec configuration proxy

```python
client = MangaCollecAPIClient(
    client_id="your_client_id",
    client_secret="your_client_secret",
    proxy={
        "http": "http://proxy-server:port",
        "https": "https://proxy-server:port"
    }
)
```

## 💻 Utilisation

### Exemple complet avec le domaine Serie

```python
import os
from mangacollec_api.client.client import MangaCollecAPIClient
from mangacollec_api.serie.endpoint.serie_endpoint import SerieEndpoint

def main():
    # Configuration du client
    client = MangaCollecAPIClient(
        client_id=os.environ.get("CLIENT_ID"),
        client_secret=os.environ.get("CLIENT_SECRET")
    )
    
    # Endpoint des séries
    serie_endpoint = SerieEndpoint(client)
    
    try:
        # API v2 - Récupérer toutes les séries (objets typés)
        series = serie_endpoint.get_all_series_v2()
        print(f"Total des séries : {len(series)}")
        
        # API v2 - Récupérer une série avec données enrichies
        if series:
            serie_complete = serie_endpoint.get_series_by_id_v2(series[0].id)
            
            # Informations de base
            serie = serie_complete.serie
            print(f"Titre: {serie.title}")
            print(f"Type: {serie_complete.type.title}")
            
            # Données associées
            print(f"Auteurs: {[author.name for author in serie_complete.authors]}")
            print(f"Éditeurs: {[pub.name for pub in serie_complete.publishers]}")
            print(f"Genres: {[kind.title for kind in serie_complete.kinds]}")
            
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
```

### Support multi-version

```python
# API v1 - Retourne des dictionnaires bruts
series_dict = serie_endpoint.get_all_series()  # Dict[str, Any]

# API v2 - Retourne des objets typés
series_objects = serie_endpoint.get_all_series_v2()  # List[Serie]
```

## 🌐 Domaines disponibles

### SerieEndpoint
```python
from mangacollec_api.serie.endpoint.serie_endpoint import SerieEndpoint

# API v1 (legacy)
series_dict = endpoint.get_all_series()
serie_dict = endpoint.get_series_by_id(serie_id)

# API v2 (moderne)
series_list = endpoint.get_all_series_v2()           # List[Serie]
serie_complete = endpoint.get_series_by_id_v2(serie_id)  # SerieEndpointEntity
```

### AuthorEndpoint
```python
from mangacollec_api.author.endpoint.author_endpoint import AuthorsEndpoint

# API v1
authors_dict = endpoint.get_all_authors()
author_dict = endpoint.get_author_by_id(author_id)

# API v2
authors_list = endpoint.get_all_authors_v2()         # List[Author]
author_complete = endpoint.get_author_by_id_v2(author_id)  # AuthorEndpointEntity
```

### Autres domaines
Tous les domaines suivent le même pattern avec des endpoints v1 et v2.

## 🧪 Tests

### Structure des tests

Le projet utilise une architecture de tests optimisée avec séparation par responsabilité :

```
src/mangacollec_api/{domain}/tests/
├── converter/              # Tests de transformation de données
├── endpoints/              # Tests d'API
│   ├── test_{domain}_endpoint_v1.py  # Tests API v1
│   └── test_{domain}_endpoint_v2.py  # Tests API v2
├── entity/                 # Tests de logique métier
└── exception/              # Tests d'exceptions
```

### Exécution des tests

```bash
# Tous les tests
poetry run pytest

# Tests d'un domaine spécifique
poetry run pytest src/mangacollec_api/serie/tests/

# Tests par version d'API
poetry run pytest src/mangacollec_api/serie/tests/endpoints/test_serie_endpoint_v1.py
poetry run pytest src/mangacollec_api/serie/tests/endpoints/test_serie_endpoint_v2.py

# Avec verbose
poetry run pytest -v

# Avec couverture
poetry run pytest --cov=src/mangacollec_api
```

### Configuration des tests

Les tests utilisent une configuration centralisée dans `pyproject.toml` :

```toml
[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["src", "tests"]
```

## 🛠️ Développement

### Installation pour le développement

```bash
git clone https://github.com/shooter-dev/mangacollec_api.git
cd mangacollec_api
poetry install
```

### Commandes de développement

```bash
# Tests
poetry run pytest

# Tests spécifiques
poetry run pytest src/mangacollec_api/serie/tests/

# Build
poetry build

# Linting (si configuré)
poetry run black .
poetry run mypy .
```

### Ajouter un nouveau domaine

1. Créer la structure du domaine :
```bash
mkdir -p src/mangacollec_api/{domain}/{endpoint,entity,converter,exception,tests}
```

2. Implémenter les interfaces :
- `endpoint/`: Définir interface et implémentation
- `entity/`: Créer entités et endpoint entities
- `converter/`: Implémenter `IConverterEntity<T>`
- `exception/`: Ajouter exceptions spécifiques
- `tests/`: Écrire tests par couche

## 📚 API Reference

### Entités principales

#### Serie
```python
@dataclass
class Serie:
    id: str                    # Identifiant unique
    title: str                 # Titre de la série
    type_id: str              # ID du type/genre
    adult_content: bool       # Contenu adulte
    editions_count: int       # Nombre d'éditions
    tasks_count: int          # Nombre de tâches
    kinds_ids: List[str]      # IDs des types associés (optionnel)
```

#### Author
```python
@dataclass  
class Author:
    id: str                    # Identifiant unique
    name: str                  # Nom de famille
    first_name: str | None     # Prénom (optionnel)
    tasks_count: int          # Nombre de tâches
```

### Endpoint Entities

Les endpoints v2 retournent des entités enrichies avec toutes les données associées :

```python
class SerieEndpointEntity:
    serie: Serie              # Série principale
    type: Genre              # Type/genre de la série
    kinds: List[Kind]        # Types associés
    tasks: List[Task]        # Tâches
    jobs: List[Job]          # Métiers
    authors: List[Author]    # Auteurs
    editions: List[Edition]  # Éditions
    publishers: List[Publisher]  # Éditeurs
    volumes: List[Volume]    # Volumes
    # ... autres relations
```

### Gestion des erreurs

```python
from mangacollec_api.core.exception.exception import (
    MangaCollecAPIError,
    NotFoundError,
    BadRequestError
)

from mangacollec_api.serie.exception.serie_exceptions import (
    SerieError,
    SerieNotFoundError,
    SerieValidationError
)

try:
    serie = serie_endpoint.get_series_by_id_v2("invalid-id")
except SerieNotFoundError as e:
    print(f"Série non trouvée: {e.serie_id}")
except NotFoundError:
    print("Ressource non trouvée")
except MangaCollecAPIError as e:
    print(f"Erreur API: {e}")
```

## 🤝 Contribution

### Workflow de contribution

1. **Fork** le projet
2. **Créer une branche** : `git checkout -b feature/nouvelle-fonctionnalite`
3. **Implémenter** en suivant l'architecture DDD
4. **Ajouter des tests** pour toutes les nouvelles fonctionnalités
5. **Tester** : `poetry run pytest`
6. **Commit** : `git commit -am 'feat: ajouter nouvelle fonctionnalité'`
7. **Push** : `git push origin feature/nouvelle-fonctionnalite`
8. **Créer une Pull Request**

### Standards de code

- **Architecture** : Suivre les principes DDD
- **Tests** : Couverture complète avec responsabilités séparées
- **Interfaces** : Utiliser les interfaces pour l'extensibilité
- **Types** : Code entièrement typé
- **Documentation** : Docstrings et commentaires appropriés

## 📄 Informations du projet

### Dépendances

**Runtime :**
- Python 3.10+
- requests ^2.32.3

**Développement :**
- pytest ^8.3.5
- pytest-mock ^3.14.0
- requests-mock ^1.12.1
- black ^25.1.0
- mypy ^1.17.0

### Versioning

Ce projet suit [Semantic Versioning](https://semver.org/).

### Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

### Contact

- **Auteur** : shooter-dev
- **Email** : vincentbleach@gmail.com
- **Repository** : [https://github.com/shooter-dev/mangacollec_api](https://github.com/shooter-dev/mangacollec_api)

---

**Note** : Cette bibliothèque n'est pas officiellement affiliée à MangaCollec. Elle fournit une interface Python pour interagir avec leur API publique.