"""Kind entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Kind:
    """Entité Kind du domaine.

    Représente un type de publication (manga, comics, BD, etc.).

    Attributes:
        id: Identifiant unique du kind
        name: Nom du type de publication
        name_en: Nom du type en anglais
    """

    id: str
    name: str
    name_en: str
