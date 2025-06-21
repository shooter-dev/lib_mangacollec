from typing import Dict, List

from mangacollec_api.converters.author_converter import AuthorConverter
from mangacollec_api.entity.author import Author


class AuthorsEndpointEntity():
    @staticmethod
    def to_list_object(data_authors: List[Dict]) -> List[Author]:
        authors: List[Author] = []

        converter = AuthorConverter()

        for author in data_authors["authors"]:
            authors.append(
                converter.deserialize(author)
            )
        return authors

class AuthorEndpointEntity():
    pass