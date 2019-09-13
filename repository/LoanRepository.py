from util.Constants import Constants


class LoanRepository:
    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, loan):
        try:
            self.cursor.execute(f'''
            INSERT INTO {Constants.Loan.TABLE} (
                {Constants.Loan.DATE_LOAN},
                {Constants.Loan.BOOK_ID},
                {Constants.Loan.USER_ID}
            ) VALUES (
                {loan.date_loan},
                {loan.book_id},
                {loan.user_id}
            )
            ''')
            return True
        except Exception as e:
            return False

    def delete(self, id):
        try:
            self.cursor.execute(f'DELETE FROM {Constants.Loan.TABLE} WHERE {Constants.Loan.ID} = {id}')
            return True
        except Exception as e:
            return False
