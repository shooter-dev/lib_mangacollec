from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    username: str
    email: Optional[str] = None
    id: Optional[str] = None

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"User(username={self.username}, id={self.id})"