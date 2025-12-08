"""In-memory edition repository."""
from src.application.dto.responses.edition_responses import GetEditionByIdV2Response
from src.domain.entities.edition import Edition
from src.domain.exceptions.edition_exceptions import EditionNotFoundException
from src.domain.repositories.edition_repository import IEditionRepository


class InMemoryEditionRepository(IEditionRepository):
    """In-memory edition repository."""

    def __init__(self) -> None:
        """Initialize the repository."""
        self._editions: dict[str, Edition] = {}

    def get_by_id_v2(self, edition_id: str) -> GetEditionByIdV2Response:
        """
        Get an edition by its id.

        Args:
            edition_id: The id of the edition.

        Returns:
            A GetEditionByIdV2Response.
        """
        if edition_id not in self._editions:
            raise EditionNotFoundException(edition_id)

        edition = self._editions[edition_id]
        return GetEditionByIdV2Response(
            editions=[edition],
            publishers=[],
            series=[],
            types=[],
            volumes=[],
        )

    def add(self, edition: Edition) -> None:
        """
        Add an edition to the repository.

        Args:
            edition: The edition to add.
        """
        self._editions[edition.id] = edition

    def clear(self) -> None:
        """Clear the repository."""
        self._editions.clear()
