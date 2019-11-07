
from src.Exceptions.BookExceptions import NotFoundException, InsertException, DeleteException, UpdateException
from src.repository.Connection import Connection
from src.util.Constants import Constants

from src.model.Book import Book
from src.model.Genre import Genre
from src.model.Collection import Collection
from src.model.Publisher import Publisher


class BookRepository:
    def get_all(self):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            SELECT * FROM {Constants.Book.TABLE}
            LEFT JOIN {Constants.Genre.TABLE}
            ON {Constants.Book.TABLE}.{Constants.Book.GENRE_ID} = {Constants.Genre.TABLE}.{Constants.Genre.ID}
            LEFT JOIN {Constants.Collection.TABLE}
            ON {Constants.Book.TABLE}.{Constants.Book.COLLECTION_ID} = {Constants.Collection.TABLE}.{Constants.Collection.ID}
            LEFT JOIN {Constants.Publisher.TABLE}
            ON {Constants.Book.TABLE}.{Constants.Book.PUBLISHER_ID} = {Constants.Publisher.TABLE}.{Constants.Publisher.ID}
            ''')
            books = []
            for x in cursor.fetchall():
                book = Book(
                    x[Constants.Book.ID],
                    x[Constants.Book.TITLE],
                    x[Constants.Book.PAGES],
                    x[Constants.Book.VALUE_MULCT]
                )
                book.publisher = Publisher(x[Constants.Publisher.ID], x[Constants.Publisher.NAME])
                book.collection = Collection(x[Constants.Collection.ID], x[Constants.Collection.NAME])
                book.genre = Genre(x[Constants.Genre.ID], x[Constants.Genre.DESCRIPTION])
                books.append(book)
            return books
        except Exception as e:
            raise NotFoundException
        finally:
            Connection.close()

    def get(self, book_id):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            SELECT * FROM {Constants.Book.TABLE}
            LEFT JOIN {Constants.Genre.TABLE}
            ON {Constants.Book.TABLE}.{Constants.Book.GENRE_ID} = {Constants.Genre.TABLE}.{Constants.Genre.ID}
            LEFT JOIN {Constants.Collection.TABLE}
            ON {Constants.Book.TABLE}.{Constants.Book.COLLECTION_ID} = {Constants.Collection.TABLE}.{Constants.Collection.ID}
            LEFT JOIN {Constants.Publisher.TABLE}
            ON {Constants.Book.TABLE}.{Constants.Book.PUBLISHER_ID} = {Constants.Publisher.TABLE}.{Constants.Publisher.ID}
            WHERE {Constants.Book.ID} = {book_id} 
            ''')
            books = []
            for x in cursor.fetchall():
                book = Book(
                    x[Constants.Book.ID],
                    x[Constants.Book.TITLE],
                    x[Constants.Book.PAGES],
                    x[Constants.Book.VALUE_MULCT]
                )
                book.publisher = Publisher(x[Constants.Publisher.ID], x[Constants.Publisher.NAME])
                book.collection = Collection(x[Constants.Collection.ID], x[Constants.Collection.NAME])
                book.genre = Genre(x[Constants.Genre.ID], x[Constants.Genre.DESCRIPTION])
                books.append(book)
            return books[0]
        except Exception as e:
            raise NotFoundException
        finally:
            Connection.close()

    def insert(self, book):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            INSERT INTO {Constants.Book.TABLE} (
                {Constants.Book.TITLE},
                {Constants.Book.PAGES},
                {Constants.Book.VALUE_MULCT},
                {Constants.Book.PUBLISHER_ID},
                {Constants.Book.COLLECTION_ID},
                {Constants.Book.GENRE_ID}
            ) VALUES(
                "{book.title}",
                {book.pages},
                {book.value_mulct},
                {book.publisher.id},
                {book.collection.id},
                {book.genre.id}
            )
            ''')
        except Exception as e:
            raise InsertException
        finally:
            Connection.close()

    def update(self, book):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            UPDATE {Constants.Book.TABLE}
            SET {Constants.Book.TITLE} = "{book.title}",
                {Constants.Book.PAGES} = {book.pages},
                {Constants.Book.VALUE_MULCT} = {book.value_mulct},
                {Constants.Book.PUBLISHER_ID} = {book.publisher.id},
                {Constants.Book.COLLECTION_ID} = {book.collection.id},
                {Constants.Book.GENRE_ID} = {book.genre.id}
            WHERE {Constants.Book.ID} = {book.id}
            ''')
        except Exception as e:
            raise UpdateException
        finally:
            Connection.close()

    def delete(self, id):
        cursor = Connection.open()
        try:
            cursor.execute(f'DELETE FROM {Constants.Book.TABLE} WHERE {Constants.Book.ID} = {id}')
        except Exception as e:
            raise DeleteException
        finally:
            Connection.close()


book_repository = BookRepository()
