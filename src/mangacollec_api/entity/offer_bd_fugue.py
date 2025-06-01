from dataclasses import dataclass

from mangacollec_api.entity.offer_abstract import AOffer

@dataclass
class OfferBdFugue(AOffer):
    isbn: str