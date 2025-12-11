"""Exceptions pour la ressource Offer.

This module contains custom exceptions for Offer-related operations.
"""

from mangacollec.domain.exceptions.base_exceptions import MangacollecException


class AmazonOfferNotFoundException(MangacollecException):
    def __init__(self, volume_asin: str) -> None:
        self.volume_asin = volume_asin
        super().__init__(f"Amazon offer with ASIN '{volume_asin}' not found.")


class BDFugueOfferNotFoundException(MangacollecException):
    def __init__(self, volume_isbn: str) -> None:
        self.volume_isbn = volume_isbn
        super().__init__(f"BDFugue offer with ISBN '{volume_isbn}' not found.")
