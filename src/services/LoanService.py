from datetime import datetime

from src.Exceptions.LoanExceptions import InvalidDateDevolution, InvalidUser, InvalidBook, IvalidDateLoan, UpdateException, IvalidDateDevolution


class LoanService:
    def __init__(self, repository):
        self.repository = repository

    def insert(self, loan):
        try:
            loan['date_loan'] = str(datetime.now())
            self.repository.insert(loan)
            return 'Empréstimo executado com sucesso'
        except IvalidDateLoan as e:
            return e

    def update(self, loan):
        self.repository.update(loan)
        return 'Empréstimo finalizado com sucesso'
