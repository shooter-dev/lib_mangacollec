"""Tests for API TypeSerie repository."""

from unittest.mock import MagicMock

import pytest

from mangacollec.domain.exceptions import TypeSerieRetrievalException
from mangacollec.infrastructure.repositories import APITypeSerieRepository


def test_get_all_types_v1_success():
    """Test récupération réussie de tous les types."""
    # Mock du client API
    mock_client = MagicMock()
    mock_client.get.return_value = [
        {"id": "1", "title": "Manga", "to_display": True},
        {"id": "2", "title": "Manhwa", "to_display": False},
    ]

    repo = APITypeSerieRepository(mock_client)

    result = repo.get_all_types_v1()

    assert len(result.types) == 2
    assert result.types[0].id == "1"
    assert result.types[0].title == "Manga"
    assert result.types[0].to_display is True
    assert result.types[1].id == "2"
    assert result.types[1].title == "Manhwa"
    assert result.types[1].to_display is False
    mock_client.get.assert_called_once_with("/v1/types")


def test_get_all_types_v1_empty():
    """Test récupération avec réponse vide."""
    mock_client = MagicMock()
    mock_client.get.return_value = []

    repo = APITypeSerieRepository(mock_client)

    result = repo.get_all_types_v1()

    assert len(result.types) == 0
    mock_client.get.assert_called_once_with("/v1/types")


def test_get_all_types_v1_api_error():
    """Test gestion d'erreur lors de l'appel API."""
    mock_client = MagicMock()
    mock_client.get.side_effect = Exception("API Error")

    repo = APITypeSerieRepository(mock_client)

    with pytest.raises(TypeSerieRetrievalException) as exc_info:
        repo.get_all_types_v1()

    assert "API Error" in str(exc_info.value)
    mock_client.get.assert_called_once_with("/v1/types")
