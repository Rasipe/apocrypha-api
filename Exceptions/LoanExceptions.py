class InvalidDateDevolution(Exception):
    def __init__(self):
        Exception.__init__(self, 'Data e devolução invalida')


class InvalidUser(Exception):
    def __init__(self):
        Exception.__init__(self, 'Usuário inválido')


class InvalidBook(Exception):
    def __init__(self):
        Exception.__init__(self, 'Livro ivalido')


class IvalidDateLoan(Exception):
    def __init__(self):
        Exception.__init__(self, 'Data do emprestimo invalida')
