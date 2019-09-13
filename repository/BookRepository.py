from util.Constants import Constants

from model.Book import Book
from model.Genre import Genre
from model.Collection import Collection
from model.Publisher import Publisher
from model.Loan import Loan
from model.User import User


class BookRepository:
    def __init__(self, cursor):
        self.cursor = cursor
        self.cursor.execute(f'''
        INSERT INTO {Constants.Book.TABLE} VALUES (
            1,
            "livro",
            5,
            2.5,
            1,
            1,
            1)
        ''')
        self.cursor.execute(f'''
        INSERT INTO {Constants.Book.TABLE} VALUES (
            2,
            "livro 2",
            25,
            5,
            1,
            1,
            1)
        ''')

    def get_all(self):
        self.cursor.execute(f'''
        SELECT * FROM {Constants.Book.TABLE}
        LEFT JOIN {Constants.Genre.TABLE}
        ON {Constants.Book.TABLE}.{Constants.Book.GENRE_ID} = {Constants.Genre.TABLE}.{Constants.Genre.ID}
        LEFT JOIN {Constants.Collection.TABLE}
        ON {Constants.Book.TABLE}.{Constants.Book.COLLECTION_ID} = {Constants.Collection.TABLE}.{Constants.Collection.ID}
        LEFT JOIN {Constants.Publisher.TABLE}
        ON {Constants.Book.TABLE}.{Constants.Book.PUBLISHER_ID} = {Constants.Publisher.TABLE}.{Constants.Publisher.ID}
        ''')
        books = []
        for x in self.cursor.fetchall():
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
        for book in books:
            self.cursor.execute(f'''
            SELECT * FROM {Constants.Loan.TABLE}
            LEFT JOIN {Constants.User.TABLE}
            ON {Constants.Loan.TABLE}.{Constants.Loan.USER_ID} = {Constants.User.TABLE}.{Constants.User.ID}
            WHERE {Constants.Loan.BOOK_ID} = {book.id}
            ''')
            for x in self.cursor.fetchall():
                loan = Loan(x[Constants.Loan.ID], x[Constants.Loan.DATE_LOAN], x[Constants.Loan.DATE_DEVOLUTION])
                loan.user = User(
                    x[Constants.User.ID],
                    x[Constants.User.NAME],
                    x[Constants.User.PHONE],
                    x[Constants.User.EMAIL]
                )
                book.loans.append(loan)
        return books

    def insert(self, book):
        try:
            self.cursor.execute(f'''
            INSERT INTO {Constants.Book.TABLE} VALUES (
                {book.title},
                {book.pages},
                {book.value_mulct},
                {book.publisher.id},
                {book.collection.id},
                {book.genre.id}
            )
            ''')
            return True
        except Exception as e:
            return False

    def update(self, book):
        try:
            self.cursor.execute(f'''
            UPDATE {Constants.Book.TABLE}
            SET {Constants.Book.TITLE} = {book.title},
                {Constants.Book.PAGES} = {book.pages},
                {Constants.Book.VALUE_MULCT} = {book.value_mulct},
                {Constants.Book.PUBLISHER_ID} = {book.publisher},
                {Constants.Book.COLLECTION_ID} = {book.collection},
                {Constants.Book.GENRE_ID} = {book.genre}
            ''')
            return True
        except Exception as e:
            return False

    def delete(self, id):
        try:
            self.cursor.execute(f'DELETE FROM {Constants.Book.TABLE} WHERE {Constants.Book.ID} = {id}')
            return True
        except Exception as e:
            return False
