from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    genre: str
    release_year: int
    id: int = None
