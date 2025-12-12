"""Tests for TypeSerie response DTOs."""

from mangacollec.application.dto import GetAllTypesSerieV1Response
from mangacollec.domain.entities import TypeSerie


def test_get_all_types_serie_v1_response_creation():
    """Test création de GetAllTypesSerieV1Response."""
    type1 = TypeSerie(id="1", title="Manga", to_display=True)
    type2 = TypeSerie(id="2", title="Manhwa", to_display=False)

    response = GetAllTypesSerieV1Response(types=[type1, type2])

    assert len(response.types) == 2
    assert response.types[0] == type1
    assert response.types[1] == type2


def test_get_all_types_serie_v1_response_empty():
    """Test création de GetAllTypesSerieV1Response vide."""
    response = GetAllTypesSerieV1Response(types=[])

    assert len(response.types) == 0
    assert response.types == []
