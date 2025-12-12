"""Tests pour les entités User et UserCollection.

This module contains unit tests for User and UserCollection entities.
"""

import pytest

from mangacollec.domain.entities import User, UserCollection


class TestUser:
    """Tests pour l'entité User."""

    def test_create_user_with_all_fields(self) -> None:
        """Test de création d'un utilisateur avec tous les champs."""
        user = User(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            username="shooterdev",
            email="shooter@example.com",
            first_name="John",
            last_name="Doe",
            avatar_url="https://example.com/avatar.jpg",
        )

        assert user.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert user.username == "shooterdev"
        assert user.email == "shooter@example.com"
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.avatar_url == "https://example.com/avatar.jpg"

    def test_create_user_minimal(self) -> None:
        """Test de création d'un utilisateur avec les champs minimaux."""
        user = User(
            id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
            username="boichi",
        )

        assert user.id == "d7f7a8a1-0543-462f-91ca-c4229f0c8108"
        assert user.username == "boichi"
        assert user.email is None
        assert user.first_name is None
        assert user.last_name is None
        assert user.avatar_url is None

    def test_create_user_without_avatar(self) -> None:
        """Test de création d'un utilisateur sans avatar."""
        user = User(
            id="test-id",
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            avatar_url=None,
        )

        assert user.avatar_url is None

    def test_user_is_frozen(self) -> None:
        """Test que l'entité User est immuable."""
        user = User(
            id="test-id",
            username="testuser",
            email="test@example.com",
        )

        with pytest.raises(AttributeError):
            user.username = "newuser"


class TestUserCollection:
    """Tests pour l'entité UserCollection."""

    def test_create_user_collection_with_all_fields(self) -> None:
        """Test de création d'une collection utilisateur avec tous les champs."""
        collection = UserCollection(
            id="collection-123",
            user_id="user-456",
            total_editions=150,
            total_volumes=1250,
            total_series=45,
            last_updated="2025-12-12T10:00:00Z",
        )

        assert collection.id == "collection-123"
        assert collection.user_id == "user-456"
        assert collection.total_editions == 150
        assert collection.total_volumes == 1250
        assert collection.total_series == 45
        assert collection.last_updated == "2025-12-12T10:00:00Z"

    def test_create_user_collection_minimal(self) -> None:
        """Test de création d'une collection utilisateur avec les champs minimaux."""
        collection = UserCollection(
            id="collection-789",
            user_id="user-101",
        )

        assert collection.id == "collection-789"
        assert collection.user_id == "user-101"
        assert collection.total_editions == 0
        assert collection.total_volumes == 0
        assert collection.total_series == 0
        assert collection.last_updated is None

    def test_create_user_collection_without_last_updated(self) -> None:
        """Test de création d'une collection utilisateur sans date de mise à jour."""
        collection = UserCollection(
            id="collection-min",
            user_id="user-min",
            total_editions=25,
            total_volumes=300,
            total_series=10,
        )

        assert collection.last_updated is None
        assert collection.total_editions == 25

    def test_user_collection_is_frozen(self) -> None:
        """Test que l'entité UserCollection est immuable."""
        collection = UserCollection(
            id="test-collection",
            user_id="test-user",
            total_editions=100,
        )

        with pytest.raises(AttributeError):
            collection.total_editions = 200

    def test_user_collection_zero_values(self) -> None:
        """Test de création d'une collection utilisateur avec des valeurs nulles."""
        collection = UserCollection(
            id="empty-collection",
            user_id="new-user",
            total_editions=0,
            total_volumes=0,
            total_series=0,
        )

        assert collection.total_editions == 0
        assert collection.total_volumes == 0
        assert collection.total_series == 0

    def test_user_collection_large_values(self) -> None:
        """Test de création d'une collection utilisateur avec de grandes valeurs."""
        collection = UserCollection(
            id="large-collection",
            user_id="collector-user",
            total_editions=1000,
            total_volumes=15000,
            total_series=500,
        )

        assert collection.total_editions == 1000
        assert collection.total_volumes == 15000
        assert collection.total_series == 500
