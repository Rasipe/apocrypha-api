from src.util.Constants import Constants
from src.repository import Connection
from src.Exceptions.LoanExceptions import InsertException, UpdateException
from datetime import datetime


class LoanRepository:

    def insert(self, loan):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            INSERT INTO {Constants.Loan.TABLE} (
                {Constants.Loan.DATE_LOAN},
                {Constants.Loan.BOOK_ID},
                {Constants.Loan.USER_ID}
            ) VALUES (
                "{loan['date_loan']}",
                {loan['book_id']},
                {loan['user_id']}
            )
            ''')
        except Exception as e:
            raise InsertException
        finally:
            Connection.close()

    def update(self, loan_id):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            UPDATE {Constants.Loan.TABLE}
            SET {Constants.Loan.DATE_DEVOLUTION} = "{datetime.now()}"
            WHERE {Constants.Loan.ID} = {loan_id}''')
        except Exception as e:
            raise UpdateException
        finally:
            Connection.close()
