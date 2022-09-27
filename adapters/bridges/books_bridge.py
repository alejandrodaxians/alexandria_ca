from typing import List, Dict

from adapters.database.schemas import Book
from adapters.connectors.book_connector import BookDBConnector


book_db = BookDBConnector()


def get_all_books() -> List[Book]:
    """
    **Display all books currently in the database**

    Parameters: None

    Returns:
        List of dicts with every book recorded.
    """
    return book_db.get_all_books()


def get_book_by_id(id) -> Dict:
    """
    **Display the book with the given id**

    Parameters:

    **id**: id, primary key of the book to get.

    Returns:
        Dict with the book information.
    """
    result = book_db.get_book_by_id(id)
    return result


def get_book_by_title(title: str) -> List[Book]:
    """
    **Display all the books which names contain the keyword passed**

    Parameters:

    **title**: The keyword with which to search for the book title.
    Must be at least 3 char long.

    Returns:
        List of dicts with every book concurrent to the keyword.
    """
    return conn.execute(books.__table__.select().where(books.__table__.c.title.contains(title))).fetchall()


def create_book(book: Book) -> Dict:
    """
    **Create a new book**

    Parameters:

    **book**: An object used to accesed the parameters needed to create the book.
    These are: title(str), author(str), genre(str), release_year(int).

    Returns:
        Dict with the new book's information.
    """
    query = books.__table__.insert().values(
        title=book.title,
        author=book.author,
        genre=book.genre,
        release_year=book.release_year,
    )
    conn.execute(query)
    return book


def delete_book(id: int) -> Dict:
    """
    **Delete a book by id**

    Parameters:

    **id**: The primary key of the book to be deleted.

    Returns:
        A Dict containing a message telling the user the book has been succesfully deleted.
    """
    conn.execute(books.__table__.select().where(books.__table__.c.id == id)).first()
    conn.execute(books.__table__.delete().where(books.__table__.c.id == id))
    return {"message": f'Book with id: {id}, deleted'}


def update_book(id: int, book: Book) -> Dict:
    """
    **Update a book by id**

    Parameters:

    **id**: The id of the book to be updated.
    **book**: An object used to accesed the parameters needed to update the book.
    These are: title(str), author(str), genre(str), release_year(int).

    Returns:
        A Dict containing a message telling the user the book has been succesfully updated.
    """
    exists = conn.execute(books.__table__.select().where(books.__table__.c.id == id)).first()
    query = books.__table__.update().where(books.__table__.c.id == id).values(
            title=book.title if book.title is not None else exists.title,
            author=book.author if book.author is not None else exists.author,
            genre=book.genre if book.genre is not None else exists.genre,
            release_year=book.release_year if book.release_year is not None else exists.release_year
        )
    conn.execute(query)
    return {"message": f"Book with id: {id}, updated succesfully."}
