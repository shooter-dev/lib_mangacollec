from dataclasses import dataclass
from abc import ABC

@dataclass
class AOffer(ABC):
    formatted_price: float
    availability: str
    merchant: str
    store_link: str
