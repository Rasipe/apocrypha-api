from Exceptions.LoanExceptions import InvalidDateDevolution, InvalidUser, InvalidBook, IvalidDateLoan


class LoanService:
    def __init__(self, repository):
        self.repository = repository

    def insert(self, loan):
        try:
            self.validate(loan)
            self.repository.insert(loan)
            return 'Empréstimo executado com sucesso'
        except IvalidDateLoan as e:
            return e
        except InvalidBook as e:
            return e
        except InvalidUser as e:
            return e

    def update(self, loan):
        try:
            if loan.date_devolution == '':
                raise InvalidDateDevolution
            self.validate(loan)
            self.repository.update(loan)
            return 'Empréstimo executado com sucesso'
        except InvalidDateDevolution as e:
            return e
        except IvalidDateLoan as e:
            return e
        except InvalidBook as e:
            return e
        except InvalidUser as e:
            return e

    def validate(self, loan):
        if loan.date_loan == '':
            raise IvalidDateLoan
        if not hasattr(loan.user, 'id'):
            raise InvalidUser
        if not hasattr(loan.book, 'id'):
            raise InvalidBook
