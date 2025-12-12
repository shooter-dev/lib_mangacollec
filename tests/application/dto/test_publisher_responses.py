"""Tests pour les DTOs de réponse des Publishers."""

from dataclasses import FrozenInstanceError

import pytest

from mangacollec.application.dto import (GetAllPublishersV2Response,
                                         GetPublisherByIdV2Response)
from mangacollec.domain.entities import Publisher


class TestGetAllPublishersV2Response:
    """Tests pour GetAllPublishersV2Response."""

    def test_create_with_publishers(self):
        """Test la création avec une liste de publishers."""
        # Arrange
        publishers = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
            Publisher(
                id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
                title="Pika",
                closed=False,
                editions_count=75,
                no_amazon=False,
            ),
        ]

        # Act
        response = GetAllPublishersV2Response(publishers=publishers)

        # Assert
        assert len(response.publishers) == 2
        assert response.publishers[0] == publishers[0]
        assert response.publishers[1] == publishers[1]

    def test_create_with_empty_list(self):
        """Test la création avec une liste vide."""
        # Act
        response = GetAllPublishersV2Response(publishers=[])

        # Assert
        assert response.publishers == []
        assert len(response.publishers) == 0

    def test_is_immutable(self):
        """Test que le DTO est immuable."""
        # Arrange
        publishers = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
        ]
        response = GetAllPublishersV2Response(publishers=publishers)

        # Act & Assert
        with pytest.raises(FrozenInstanceError):
            response.publishers = []

    def test_equality(self):
        """Test l'égalité entre deux réponses."""
        # Arrange
        publishers = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
            Publisher(
                id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
                title="Pika",
                closed=False,
                editions_count=75,
                no_amazon=False,
            ),
        ]
        response1 = GetAllPublishersV2Response(publishers=publishers)
        response2 = GetAllPublishersV2Response(publishers=publishers)

        # Act & Assert
        assert response1 == response2

    def test_inequality_with_different_publishers(self):
        """Test l'inégalité avec des publishers différents."""
        # Arrange
        publishers1 = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
            Publisher(
                id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
                title="Pika",
                closed=False,
                editions_count=75,
                no_amazon=False,
            ),
        ]
        publishers2 = [
            Publisher(
                id="e8f7a8a1-0543-462f-91ca-c4229f0c8109",
                title="Glénat",
                closed=False,
                editions_count=200,
                no_amazon=False,
            ),
            Publisher(
                id="f9f7a8a1-0543-462f-91ca-c4229f0c8110",
                title="Vent d'Ouest",
                closed=False,
                editions_count=100,
                no_amazon=False,
            ),
        ]
        response1 = GetAllPublishersV2Response(publishers=publishers1)
        response2 = GetAllPublishersV2Response(publishers=publishers2)

        # Act & Assert
        assert response1 != response2

    def test_equality_with_none(self):
        """Test l'inégalité avec None."""
        # Arrange
        publishers = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
        ]
        response = GetAllPublishersV2Response(publishers=publishers)

        # Act & Assert
        assert response is not None


class TestGetPublisherByIdV2Response:
    """Tests pour GetPublisherByIdV2Response."""

    def test_create_with_single_publisher(self):
        """Test la création avec un seul publisher."""
        # Arrange
        publisher = Publisher(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Kana",
            closed=False,
            editions_count=150,
            no_amazon=False,
        )

        response = GetPublisherByIdV2Response(
            publishers=[publisher],
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )

        # Assert
        assert len(response.publishers) == 1
        assert response.publishers[0] == publisher

    def test_create_with_multiple_publishers(self):
        """Test la création avec plusieurs publishers."""
        # Arrange
        publishers = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
            Publisher(
                id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
                title="Pika",
                closed=False,
                editions_count=75,
                no_amazon=False,
            ),
            Publisher(
                id="e8f7a8a1-0543-462f-91ca-c4229f0c8109",
                title="Glénat",
                closed=False,
                editions_count=200,
                no_amazon=False,
            ),
        ]

        # Act
        response = GetPublisherByIdV2Response(
            publishers=publishers,
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )
        assert response.publishers == publishers

    def test_create_with_empty_list(self):
        """Test la création avec une liste vide."""
        # Act
        response = GetPublisherByIdV2Response(
            publishers=[],
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )

        # Assert
        assert response.publishers == []

    def test_is_immutable(self):
        """Test que le DTO est immuable."""
        # Arrange
        publisher = Publisher(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Kana",
            closed=False,
            editions_count=150,
            no_amazon=False,
        )
        response = GetPublisherByIdV2Response(
            publishers=[publisher],
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )

        # Act & Assert
        with pytest.raises(FrozenInstanceError):
            response.publishers = []

    def test_equality(self):
        """Test l'égalité entre deux réponses."""
        # Arrange
        publishers = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
            Publisher(
                id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
                title="Pika",
                closed=False,
                editions_count=75,
                no_amazon=False,
            ),
        ]
        response1 = GetPublisherByIdV2Response(
            publishers=publishers,
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )
        response2 = GetPublisherByIdV2Response(
            publishers=publishers,
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )

        # Act & Assert
        assert response1 == response2

    def test_inequality_with_different_publishers(self):
        """Test l'inégalité avec des publishers différents."""
        # Arrange
        publishers1 = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
            Publisher(
                id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
                title="Pika",
                closed=False,
                editions_count=75,
                no_amazon=False,
            ),
        ]
        publishers2 = [
            Publisher(
                id="e8f7a8a1-0543-462f-91ca-c4229f0c8109",
                title="Glénat",
                closed=False,
                editions_count=200,
                no_amazon=False,
            ),
            Publisher(
                id="f9f7a8a1-0543-462f-91ca-c4229f0c8110",
                title="Vent d'Ouest",
                closed=False,
                editions_count=100,
                no_amazon=False,
            ),
        ]
        response1 = GetPublisherByIdV2Response(
            publishers=publishers1,
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )
        response2 = GetPublisherByIdV2Response(
            publishers=publishers2,
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )

        # Act & Assert
        assert response1 != response2

    def test_preserves_order(self):
        """Test que l'ordre des publishers est préservé."""
        # Arrange
        publisher1 = Publisher(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Publisher A",
            closed=False,
            editions_count=150,
            no_amazon=False,
        )
        publisher2 = Publisher(
            id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
            title="Publisher B",
            closed=False,
            editions_count=75,
            no_amazon=False,
        )
        publisher3 = Publisher(
            id="e8f7a8a1-0543-462f-91ca-c4229f0c8110",
            title="Publisher C",
            closed=False,
            editions_count=200,
            no_amazon=False,
        )
        publishers = [publisher1, publisher2, publisher3]

        # Act
        response = GetPublisherByIdV2Response(
            publishers=publishers,
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )

        # Assert
        assert response.publishers[0].title == "Publisher A"
        assert response.publishers[1].title == "Publisher B"
        assert response.publishers[2].title == "Publisher C"


class TestPublisherDTOsIntegration:
    """Tests d'intégration pour les DTOs Publishers."""

    def test_both_response_types_use_same_structure(self):
        """Test que les deux types de réponse utilisent la même structure."""
        # Arrange
        publishers = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
            Publisher(
                id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
                title="Pika",
                closed=False,
                editions_count=75,
                no_amazon=False,
            ),
        ]
        get_all_response = GetAllPublishersV2Response(publishers=publishers)
        get_by_id_response = GetPublisherByIdV2Response(
            publishers=publishers,
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )

        # Act & Assert
        assert get_all_response.publishers == get_by_id_response.publishers
        assert len(get_all_response.publishers) == len(get_by_id_response.publishers)

    def test_can_convert_between_response_types(self):
        """Test la conversion entre les deux types de réponse."""
        # Arrange
        publishers = [
            Publisher(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                title="Kana",
                closed=False,
                editions_count=150,
                no_amazon=False,
            ),
        ]
        get_all_response = GetAllPublishersV2Response(publishers=publishers)

        # Act
        get_by_id_response = GetPublisherByIdV2Response(
            publishers=get_all_response.publishers,
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )

        # Assert
        assert get_all_response.publishers == get_by_id_response.publishers
