"""Tests unitaires pour l'entité Job."""

import pytest

from src.domain.entities.job import Job


class TestJobEntity:
    """Tests pour l'entité Job."""

    def test_job_creation(self):
        """Test la création d'un job."""
        # Act
        job = Job(id="1", title="Auteur")

        # Assert
        assert job.id == "1"
        assert job.title == "Auteur"

    def test_job_immutability(self):
        """Test que Job est immuable."""
        # Arrange
        job = Job(id="1", title="Auteur")

        # Act & Assert
        with pytest.raises(Exception):  # FrozenInstanceError
            job.id = "2"

    def test_job_equality(self):
        """Test l'égalité entre deux jobs identiques."""
        # Arrange
        job1 = Job(id="1", title="Auteur")
        job2 = Job(id="1", title="Auteur")

        # Assert
        assert job1 == job2

    def test_job_inequality(self):
        """Test l'inégalité entre deux jobs différents."""
        # Arrange
        job1 = Job(id="1", title="Auteur")
        job2 = Job(id="2", title="Dessinateur")

        # Assert
        assert job1 != job2

    def test_job_with_special_characters(self):
        """Test la création d'un job avec des caractères spéciaux."""
        # Act
        job = Job(id="uuid-123", title="Œuvre originale")

        # Assert
        assert job.id == "uuid-123"
        assert job.title == "Œuvre originale"
