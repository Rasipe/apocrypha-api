class InvalidId(Exception):
    def __init__(self):
        Exception.__init__(self, 'Usuário não encontrado')


class InvalidUserName(Exception):
    def __init__(self):
        Exception.__init__(self, 'Nome de usuário invalido')


class InvalidEmail(Exception):
    def __init__(self):
        Exception.__init__(self, 'Email de usuário invalido')


class InvalidPhone(Exception):
    def __init__(self):
        Exception.__init__(self, 'Telefone de usuário invalido')