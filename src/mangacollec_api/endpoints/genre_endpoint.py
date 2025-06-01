from mangacollec_api.interfaces.endpoints.genre_endpoint_interface import IGenresEndpoint


class GenresEndpoint(IGenresEndpoint):
    """
    Implémentation des opérations pour les genres de mangas dans l'API MangaCollec.
    """

    def get_all_genres(self) -> dict:
        """
        Récupère la liste complète des genres de mangas disponibles sur MangaCollec.

        :return: Liste des genres
        """
        return self.client.get("/v1/types")
