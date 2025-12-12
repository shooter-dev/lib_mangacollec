"""Tests for TypeSerie use cases."""

from mangacollec.application.dto import GetAllTypesSerieV1Response
from mangacollec.application.use_cases import GetAllTypesSerieV1UseCase
from mangacollec.domain.entities import TypeSerie
from mangacollec.infrastructure.repositories import InMemoryTypeSerieRepository


def test_get_all_types_serie_v1_usecase():
    """Test du use case GetAllTypesSerieV1UseCase."""
    # Arrange
    repo = InMemoryTypeSerieRepository()
    type1 = TypeSerie(id="1", title="Manga", to_display=True)
    type2 = TypeSerie(id="2", title="Manhwa", to_display=False)
    repo.add(type1)
    repo.add(type2)

    usecase = GetAllTypesSerieV1UseCase(repo)

    # Act
    result = usecase()

    # Assert
    assert isinstance(result, GetAllTypesSerieV1Response)
    assert len(result.types) == 2
    assert type1 in result.types
    assert type2 in result.types


def test_get_all_types_serie_v1_usecase_empty():
    """Test du use case avec un repository vide."""
    # Arrange
    repo = InMemoryTypeSerieRepository()
    usecase = GetAllTypesSerieV1UseCase(repo)

    # Act
    result = usecase()

    # Assert
    assert isinstance(result, GetAllTypesSerieV1Response)
    assert len(result.types) == 0
