from util.Constants import Constants

from model.User import User
from model.Loan import Loan
from model.Book import Book
from model.Publisher import Publisher
from model.Collection import Collection
from model.Genre import Genre


class UserRepository:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_all(self):
        self.cursor.execute(f'''
        SELECT {Constants.User.ID}, {Constants.User.NAME}
        FROM {Constants.User.TABLE}
        ''')
        users = []
        for x in self.cursor.fetchall():
            users.append(User(x[Constants.User.ID], x[Constants.User.NAME]))
        return users

    def get(self, id):
        self.cursor.execute(f'''
        SELECT * FROM {Constants.User.TABLE}
        WHERE {Constants.User.ID} = {id}
        ''')
        user = {}
        for x in self.cursor.fetchall():
            user = User(
                x[Constants.User.ID],
                x[Constants.User.NAME],
                x[Constants.User.PHONE],
                x[Constants.User.EMAIL]
            )
            user.loans = self.get_loans(id)
        return user

    def get_loans(self, user_id):
        loans = []
        self.cursor.execute(f'''
        SELECT * FROM {Constants.Loan.TABLE}
        LEFT JOIN {Constants.Book.TABLE}
        ON {Constants.Book.TABLE}.{Constants.Book.ID} = {Constants.Loan.TABLE}.{Constants.Loan.BOOK_ID}
        WHERE {Constants.Loan.USER_ID} = {user_id}
        ''')
        ids = []
        for x in self.cursor.fetchall():
            loans.append(Loan(
                x[Constants.Loan.ID],
                x[Constants.Loan.DATE_LOAN],
                x[Constants.Loan.DATE_DEVOLUTION],
            ))
            ids.append(x[Constants.Book.ID])
        for i in range(len(loans)):
            self.cursor.execute(f'''
            SELECT * FROM {Constants.Book.TABLE}
            LEFT JOIN {Constants.Genre.TABLE}
            ON {Constants.Book.TABLE}.{Constants.Book.GENRE_ID} = {Constants.Genre.TABLE}.{Constants.Genre.ID}
            LEFT JOIN {Constants.Collection.TABLE}
            ON {Constants.Book.TABLE}.{Constants.Book.COLLECTION_ID} = {Constants.Collection.TABLE}.{Constants.Collection.ID}
            LEFT JOIN {Constants.Publisher.TABLE}
            ON {Constants.Book.TABLE}.{Constants.Book.PUBLISHER_ID} = {Constants.Publisher.TABLE}.{Constants.Publisher.ID}
            WHERE {Constants.Book.ID} = {ids[i]}            
            ''')
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
                loans[i].book = book
        return loans

    def insert(self, user):
        try:
            self.cursor.execute(f'''
            INSERT INTO {Constants.User.TABLE} VALUES (
                {user.name},
                {user.phone},
                {user.email}
            )
            ''')
            return True
        except Exception as e:
            return False

    def update(self, user):
        try:
            self.cursor.execute(f'''
            UPDATE {Constants.User.TABLE}
            SET {Constants.User.NAME} = {user.name},
                {Constants.User.PHONE} = {user.phone},
                {Constants.User.EMAIL} = {user.email}
            ''')
            return True
        except Exception as e:
            return False

    def delete(self, id):
        try:
            self.cursor.execute(f'DELETE FROM {Constants.User.TABLE} WHERE {Constants.User.ID} = {id}')
            return True
        except Exception as e:
            return False
