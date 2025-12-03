"""Value object ISBN pour la gestion des numéros ISBN.

Ce module implémente un value object pour la validation et la gestion
des numéros ISBN (International Standard Book Number).
----------
ISBN value object for ISBN number management.

This module implements a value object for validation and management
of ISBN (International Standard Book Number) numbers.
"""

import re


class ISBN:
    """Value object pour la représentation et validation des numéros ISBN.

    Cette classe représente un numéro ISBN avec validation automatique.
    Les ISBN sont normalisés en enlevant les tirets et les espaces.
    Seuls les ISBN-10 et ISBN-13 sont supportés.
    ----------
    Value object for ISBN representation and validation.

    This class represents an ISBN number with automatic validation.
    ISBNs are normalized by removing hyphens and spaces.
    Only ISBN-10 and ISBN-13 are supported.
    """

    def __init__(self, value: str) -> None:
        """Initialise un objet ISBN avec validation.

        Args:
            value (str): Numéro ISBN à valider.

        Raises:
            ValueError: Si le numéro ISBN n'est pas valide.

        Examples:
            >>> isbn = ISBN("978-2-123456-78-9")
            >>> str(isbn)
            '9782123456789'
            >>> isbn = ISBN("123456789X")  # ISBN-10
            >>> str(isbn)
            '123456789X'
        """
        self.value: str = value.strip().replace("-", "")
        self._validate()

    def _validate(self) -> None:
        """Valide le format du numéro ISBN.

        Vérifie que le numéro ISBN correspond à un format valide :
        - ISBN-10 : 10 chiffres
        - ISBN-13 : 13 chiffres

        Raises:
            ValueError: Si le format du numéro ISBN est invalide.

        Examples:
            >>> ISBN("9782123456789")  # Valide
            >>> ISBN("1234567890")     # Valide (ISBN-10)
            >>> ISBN("invalid")        # Lève ValueError
        """
        if not re.match(r"^\d{10}(\d{3})?$", self.value):
            raise ValueError(f"Invalid ISBN: {self.value}")

    def __str__(self) -> str:
        """Retourne la représentation sous forme de chaîne de caractères.

        Returns:
            str: Le numéro ISBN normalisé sans tirets ni espaces.

        Examples:
            >>> isbn = ISBN("978-2-123456-78-9")
            >>> str(isbn)
            '9782123456789'
        """
        # Représentation lisible
        return self.value

    def __eq__(self, other):
        """Compare deux objets ISBN pour l'égalité.

        Args:
            other: Objet à comparer.

        Returns:
            bool: True si les ISBN sont identiques, False sinon.

        Examples:
            >>> isbn1 = ISBN("9782123456789")
            >>> isbn2 = ISBN("9782123456789")
            >>> isbn3 = ISBN("1234567890")
            >>> isbn1 == isbn2
            True
            >>> isbn1 == isbn3
            False
            >>> isbn1 == "9782123456789"
            False
        """
        if not isinstance(other, ISBN):
            return False
        return self.value == other.value

    def __hash__(self):
        """Retourne le hash de l'objet ISBN.

        Returns:
            int: Hash basé sur la valeur normalisée de l'ISBN.

        Examples:
            >>> isbn1 = ISBN("9782123456789")
            >>> isbn2 = ISBN("9782123456789")
            >>> hash(isbn1) == hash(isbn2)
            True
        """
        return hash(self.value)
