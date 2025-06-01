import os
from typing import Dict

import pytest
from mangacollec_api.client import MangaCollecAPIClient
from endpoints.volume_endpoint import VolumeEndpoint


@pytest.mark.integration
def test_get_latest_volumes_news_live():
    """
    Test réel : récupération des volumes récents via l'API réelle.
    Nécessite des variables d'environnement : CLIENT_ID et CLIENT_SECRET.
    """
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    assert client_id, "CLIENT_ID non défini dans les variables d'environnement"
    assert client_secret, "CLIENT_SECRET non défini dans les variables d'environnement"

    client = MangaCollecAPIClient(client_id=client_id, client_secret=client_secret)
    volumes_api = VolumeEndpoint(client)

    response = volumes_api.get_latest_volumes_news()

    assert isinstance(response, list)


@pytest.mark.integration
def test_get_volume_live():
    """
    Test réel pour récupérer un volume spécifique en utilisant son ID.
    Nécessite une connexion valide.
    """
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    assert client_id, "CLIENT_ID non défini"
    assert client_secret, "CLIENT_SECRET non défini"
    assert username, "USERNAME non défini"
    assert password, "PASSWORD non défini"

    # Authentification via client credentials
    client = MangaCollecAPIClient(
        client_id=client_id,
        client_secret=client_secret,
        email=username,
        password=password
    )

    volumes_api = VolumeEndpoint(client)

    # Remplace par un ID de volume valide pour tester
    volume_id = "4f99ce2c-3a37-4252-9610-7b04a605d7d5"
    response = volumes_api.get_volume_by_id(volume_id)

    assert isinstance(response, Dict), "La réponse pour un volume spécifique doit être un dictionnaire"
    assert response.get("id") == volume_id, "L'ID du volume ne correspond pas"