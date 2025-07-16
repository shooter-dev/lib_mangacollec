from mangacollec_api.publisher.endpoint.publisher_endpoint_interface import IPublisherEndpoint


class PublisherEndpoint(IPublisherEndpoint):
    """
    Classe pour interagir avec l'API MangaCollec concernant les publishers.
    """

    def get_all_publishers(self):
        """
        Récupère la liste complète des publishers disponibles sur MangaCollec.

        :return: Liste des publishers.
        """
        return self.client.get("/v1/publishers")

    def get_all_publishers_v2(self):
        """
        Récupère une liste complète des publishers disponibles sur MangaCollec.

        :return: Liste des publishers.
        """
        return self.client.get("/v2/publishers")

    def get_publisher_by_id(self, publishers_id: str):
        """
        Récupère une publisher spécifique à partir de son ID.

        :param publishers_id: Identifiant de la publisher
        :return: Détails de la publisher.
        """

        return self.client.get(f"/v1/publishers/{publishers_id}")

    def get_publisher_by_id_v2(self, publishers_id: str):
        """
        Récupère un publisher spécifique à partir de son ID.

        :param publishers_id: Identifiant de la publisher
        :return: Détails du publisher.
        """

        return self.client.get(f"/v2/publishers/{publishers_id}")
