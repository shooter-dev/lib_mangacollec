import os
from typing import Dict, Any

from mangacollec_api.client import MangaCollecAPIClient
from mangacollec_api.interfaces.client.client_interface import IMangaCollecAPIClient
from mangacollec_api.interfaces.endpoints.author_endpoint_interface import IAuthorsEndpoint


class AuthorsEndpoint(IAuthorsEndpoint):
    """
    Implémentation des opérations pour les auteurs dans l'API MangaCollec.
    """

    def get_all_authors(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des auteurs disponibles sur MangaCollec.

        :return: Liste des auteurs
        """
        return self.client.get("/v1/authors")

    def get_author_by_id(self, author_id: str) -> Dict[str, Any]:
        """
        Récupère un auteur spécifique à partir de son ID.

        :param author_id: Identifiant de l'auteur
        :return: Détails de l'auteur
        """
        return self.client.get(f"/v1/authors/{author_id}")

    def get_all_authors_v2(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des auteurs disponibles sur MangaCollec (API v2).

        :return: Liste des auteurs
        """
        return self.client.get("/v2/authors")

    def get_author_by_id_v2(self, author_id: str) -> Dict[str, Any]:
        """
        Récupère un auteur spécifique à partir de son ID (API v2).

        :param author_id: Identifiant de l'auteur
        :return: Détails de l'auteur
        """
        return self.client.get(f"/v2/authors/{author_id}")


if __name__ == '__main__':
    client: IMangaCollecAPIClient = MangaCollecAPIClient(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        email=os.environ.get('USERNAME_PROD'),
        password=os.environ.get('PASSWORD')
    )

    authors_endpoint = AuthorsEndpoint(client)

    # Test des méthodes
    print("Liste des auteurs (v1):")
    print(authors_endpoint.get_all_authors())
    print("Auteur spécifique (v1):")
    print(authors_endpoint.get_author_by_id("edad2d63-cc34-42b8-9bc2-ca9e210b670d"))
    print("Liste des auteurs (v2):")
    print(authors_endpoint.get_all_authors_v2())
    print("Auteur spécifique (v2):")
    print(authors_endpoint.get_author_by_id_v2("edad2d63-cc34-42b8-9bc2-ca9e210b670d")) 