import os

import pytest
from mangacollec_api.client import MangaCollecAPIClient
from endpoints.serie_endpoint import SerieEndpoint


@pytest.mark.integration
def test_get_all_series_live():
    """
    Test réel : récupération de toutes les séries via l'API.
    """
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    assert client_id and client_secret and username and password

    client = MangaCollecAPIClient(
        client_id=client_id,
        client_secret=client_secret,
        email=username,
        password=password
    )
    series_api = SerieEndpoint(client)

    response = series_api.get_all_series()

    assert isinstance(response, list), "La réponse attendue est une liste de séries"
    assert len(response) > 0, "Aucune série n'a été récupérée"


@pytest.mark.integration
def test_get_series_by_id_live():
    """
    Test réel : récupération d'une série par son ID.
    """
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    assert client_id and client_secret and username and password

    client = MangaCollecAPIClient(
        client_id=client_id,
        client_secret=client_secret,
        email=username,
        password=password
    )
    series_api = SerieEndpoint(client)

    # Remplacer par un ID réel si besoin
    series_id = "a320ac19-4318-4471-9e4e-eb017f4584d5"
    response = series_api.get_series_by_id(series_id)

    assert isinstance(response, dict), "La réponse attendue est un dictionnaire"
    assert response.get("id") == series_id, "L'ID de la série ne correspond pas"