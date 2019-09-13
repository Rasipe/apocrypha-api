class Loan:
    def __init__(self, id, date_loan, date_devolution):
        self.id = id
        self.date_loan = date_loan
        self.date_devolution = date_devolution
        self.book = {}
        self.user = {}

    def __str__(self):
        return f'id: {self.id}' \
               f'\nData de Emprestimo: {self.date_loan}' \
               f'\nData de Devolução: {self.date_devolution}' \
               f'\nUsuario: \n{self.user}' \
               f'\nLivro: \n{self.book}'
