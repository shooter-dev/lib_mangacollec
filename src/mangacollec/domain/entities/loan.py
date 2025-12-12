"""Loan entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class LoanDeleted:
    """Entité LoanDeleted pour les prêts supprimés."""

    id: str
    deleted: bool
