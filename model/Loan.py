class Loan:
    def __init__(self, id, date_loan, date_devolution):
        self.id = id
        self.date_loan = date_loan
        self.date_devolution = date_devolution
        self.book = {}
        self.user = {}
