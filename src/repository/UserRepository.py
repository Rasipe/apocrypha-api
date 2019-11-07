from src.repository.Connection import Connection
from src.util.Constants import Constants
from src.Exceptions.UserExceptions import NotFoundException, InsertException, UpdateException, DeleteException
from src.Exceptions.LoanExceptions import NotFoundLoanException
from src.model.User import User
from src.model.Loan import Loan
from src.model.Book import Book
from src.model.Publisher import Publisher
from src.model.Collection import Collection
from src.model.Genre import Genre


class UserRepository:

    def get_all(self):
        cursor = Connection.open()
        try:
            cursor.execute(f'SELECT * FROM {Constants.User.TABLE}')
            users = []
            for x in cursor.fetchall():
                user = User(x[Constants.User.ID], x[Constants.User.NAME], x[Constants.User.PHONE], x[Constants.User.EMAIL])
                cursor.execute(f'''
                    SELECT * FROM {Constants.Loan.TABLE}
                    LEFT JOIN {Constants.Book.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.ID} = {Constants.Loan.TABLE}.{Constants.Loan.BOOK_ID}
                    WHERE {Constants.Loan.USER_ID} = {user.id}
                    AND {Constants.Loan.DATE_DEVOLUTION} IS null
                ''')
                for y in cursor.fetchall():
                    loan = Loan(
                        y[Constants.Loan.ID],
                        y[Constants.Loan.DATE_LOAN],
                        y[Constants.Loan.DATE_DEVOLUTION]
                    )
                    loan.book = Book(
                        y[Constants.Book.ID],
                        y[Constants.Book.TITLE],
                        y[Constants.Book.PAGES],
                        y[Constants.Book.VALUE_MULCT],
                    )
                    user.loans.append(loan)
                users.append(user)
            return users
        finally:
            Connection.close()

    def insert(self, user):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            INSERT INTO {Constants.User.TABLE}(
                {Constants.User.NAME},
                {Constants.User.PHONE},
                {Constants.User.EMAIL}
            ) VALUES (
                "{user.name}",
                "{user.phone}",
                "{user.email}"
            )
            ''')
        except Exception as e:
            raise InsertException
        finally:
            Connection.close()

    def update(self, user):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            UPDATE {Constants.User.TABLE}
            SET {Constants.User.NAME} = "{user.name}",
                {Constants.User.PHONE} = "{user.phone}",
                {Constants.User.EMAIL} = "{user.email}"
            WHERE {Constants.User.ID} = {user.id}
            ''')
        except Exception as e:
            raise UpdateException
        finally:
            Connection.close()

    def delete(self, id):
        cursor = Connection.open()
        try:
            cursor.execute(f'DELETE FROM {Constants.User.TABLE} WHERE {Constants.User.ID} = {id}')
        except Exception as e:
            raise DeleteException
        finally:
            Connection.close()
