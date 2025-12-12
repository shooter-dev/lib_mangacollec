"""In-memory author repository."""

from mangacollec.application.dto import GetAllAuthorsV2Response, GetAuthorByIdV2Response
from mangacollec.application.mappers import AuthorMapper
from mangacollec.domain.entities import Author, AuthorListItem
from mangacollec.domain.exceptions import AuthorNotFoundException
from mangacollec.domain.repositories import IAuthorRepository


class InMemoryAuthorRepository(IAuthorRepository):
    """In-memory author repository."""

    def __init__(self) -> None:
        """Initialize the repository."""
        self._authors: dict[str, Author] = {}

    def get_all_v2(self) -> GetAllAuthorsV2Response:
        """
        Get all authors.

        Returns:
            A GetAllAuthorsV2Response.
        """
        return GetAllAuthorsV2Response(authors=list(self._authors.values()))

    def get_by_id_v2(self, author_id: str) -> GetAuthorByIdV2Response:
        """
        Get an author by its id.

        Args:
            author_id: The id of the author.

        Returns:
            A GetAuthorByIdV2Response.
        """
        if author_id not in self._authors:
            raise AuthorNotFoundException(author_id)

        author = self._authors[author_id]
        return GetAuthorByIdV2Response(
            authors=[author],
            tasks=[],
            jobs=[],
            series=[],
            editions=[],
            volumes=[],
        )

    def get_list(self) -> list[AuthorListItem]:
        """
        Get a list of all authors.

        Returns:
            A list of AuthorListItem.
        """
        return [AuthorMapper.to_list_item(author) for author in self._authors.values()]

    def add(self, author: Author) -> None:
        """
        Add an author to the repository.

        Args:
            author: The author to add.
        """
        self._authors[author.id] = author

    def clear(self) -> None:
        """Clear the repository."""
        self._authors.clear()
