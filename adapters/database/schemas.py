from sqlalchemy import Column, Integer, String

from adapters.connectors.db_connection import DatabaseConnection


db = DatabaseConnection()
Base = db.base


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    genre = Column(String(255))
    release_year = Column(Integer)
