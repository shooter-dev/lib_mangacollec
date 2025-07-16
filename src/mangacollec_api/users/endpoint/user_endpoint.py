from typing import Dict, List

from mangacollec_api.users.endpoint.user_endpoint_interface import IUserEndpoint


class UserEndpoint(IUserEndpoint):
    """
    Classe responsable de la gestion des volumes via l'API MangaCollec.
    """

    def get_recommendation(self) -> Dict | None:
        if self.client.is_auth:
            return self.client.get("/v1/users/me/recommendation")
        return None

    def get_native_planning(self) -> Dict:
        # TODO "implemente get_native_planning"
        return self.client.get("/v1/users/?")

    def get_info_user(self) -> Dict | None:
        if self.client.is_auth:
            return self.client.get("/v1/users/me")
        return None

    def get_collection_by_username(self, username: str) -> List[Dict]:
        return self.client.get(f"/v1/user/{username}/collection")

    def get_collection_by_username_v2(self, username: str) -> List[Dict]:
        return self.client.get(f"/v2/user/{username}/collection")

    def get_collection(self) -> List[Dict] | None:
        if self.client.is_auth:
            return self.client.get("/v1/users/me/collection")
        return None

    def get_collection_v2(self) -> List[Dict] | None:
        if self.client.is_auth:
            return self.client.get("/v2/users/me/collection")
        return None
