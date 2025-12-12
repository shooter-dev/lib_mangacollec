"""Implémentation en mémoire du repository Read pour les tests.

This module provides an in-memory implementation of the Read repository for testing.
"""

from datetime import datetime, timezone

from mangacollec.application.dto import (
    CreateReadsMultipleV1Response,
    DeleteReadsMultipleV1Response,
)
from mangacollec.domain.entities import (
    Read,
    ReadDeleted,
    ReadEdition,
    ReadEditionDeleted,
)
from mangacollec.domain.exceptions import ReadCreationException, ReadDeletionException
from mangacollec.domain.repositories import IReadRepository


class InMemoryReadRepository(IReadRepository):
    """Implémentation en mémoire du repository Read (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec des dictionnaires vides."""
        self._reads: dict[str, Read] = {}
        self._read_editions: dict[str, ReadEdition] = {}
        self._next_read_id = 1
        self._next_read_edition_id = 1

    def create_reads_multiple_v1(self, volume_ids: list[str]) -> CreateReadsMultipleV1Response:
        """Crée plusieurs lectures pour les volumes donnés.

        Args:
            volume_ids: Liste des IDs de volumes à marquer comme lus

        Returns:
            CreateReadsMultipleV1Response contenant les lectures et éditions créées

        Raises:
            ReadCreationException: Si la création échoue

        Note:
            Cette implémentation simule le comportement de l'API:
            - Crée un Read pour chaque volume_id
            - Crée un ReadEdition associé (simulation auto-follow)
        """
        try:
            created_reads: list[Read] = []
            created_read_editions: list[ReadEdition] = []

            for volume_id in volume_ids:
                # Créer le Read
                read = Read(
                    id=str(self._next_read_id),
                    user_id="test_user",
                    volume_id=volume_id,
                    created_at=datetime.now(timezone.utc),
                )
                self._reads[read.id] = read
                created_reads.append(read)
                self._next_read_id += 1

                # Créer le ReadEdition associé (auto-follow)
                read_edition = ReadEdition(
                    id=str(self._next_read_edition_id),
                    edition_id=f"edition_{volume_id}",  # Simulation
                    user_id="test_user",
                    reading=True,
                    created_at=datetime.now(timezone.utc),
                )
                self._read_editions[read_edition.id] = read_edition
                created_read_editions.append(read_edition)
                self._next_read_edition_id += 1

            return CreateReadsMultipleV1Response(reads=created_reads, read_editions=created_read_editions)
        except Exception as e:
            raise ReadCreationException(volume_ids, str(e)) from e

    def delete_reads_multiple_v1(self, read_ids: list[str]) -> DeleteReadsMultipleV1Response:
        """Supprime plusieurs lectures.

        Args:
            read_ids: Liste des IDs de lectures à supprimer

        Returns:
            DeleteReadsMultipleV1Response contenant les lectures et éditions supprimées

        Raises:
            ReadDeletionException: Si la suppression échoue

        Note:
            Cette implémentation simule le comportement de l'API:
            - Supprime les Reads
            - Supprime les ReadEditions associées
        """
        try:
            deleted_reads: list[ReadDeleted] = []
            deleted_read_editions: list[ReadEditionDeleted] = []

            for read_id in read_ids:
                # Vérifier que le Read existe
                if read_id not in self._reads:
                    deleted_reads.append(ReadDeleted(id=read_id, deleted=False))
                    continue

                # Supprimer le Read
                del self._reads[read_id]
                deleted_reads.append(ReadDeleted(id=read_id, deleted=True))

                # Supprimer les ReadEditions associées (simulation)
                # Dans un vrai système, on rechercherait les ReadEditions liées
                for read_edition_id in list(self._read_editions.keys()):
                    del self._read_editions[read_edition_id]
                    deleted_read_editions.append(ReadEditionDeleted(id=read_edition_id, deleted=True))
                    break  # Simuler 1 édition par lecture

            return DeleteReadsMultipleV1Response(reads=deleted_reads, read_editions=deleted_read_editions)
        except Exception as e:
            raise ReadDeletionException(read_ids, str(e)) from e

    def add_read(self, read: Read) -> Read:
        """Ajoute une lecture au repository (méthode pour les tests).

        Args:
            read: Entité Read à ajouter

        Returns:
            L'entité Read ajoutée
        """
        self._reads[read.id] = read
        return read

    def add_read_edition(self, read_edition: ReadEdition) -> ReadEdition:
        """Ajoute une lecture d'édition au repository (méthode pour les tests).

        Args:
            read_edition: Entité ReadEdition à ajouter

        Returns:
            L'entité ReadEdition ajoutée
        """
        self._read_editions[read_edition.id] = read_edition
        return read_edition

    def clear(self) -> None:
        """Vide le repository (méthode pour les tests)."""
        self._reads.clear()
        self._read_editions.clear()
        self._next_read_id = 1
        self._next_read_edition_id = 1
