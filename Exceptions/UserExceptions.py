class InvalidUserName(Exception):
    def __init__(self):
        Exception.__init__(self, 'Nome de usuário invalido')


class InvalidEmail(Exception):
    def __init__(self):
        Exception.__init__(self, 'Email de usuário invalido')


class InvalidPhone(Exception):
    def __init__(self):
        Exception.__init__(self, 'Telefone de usuário invalido')


class NotFoundException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Usuário não encontrado')


class InsertException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel inserir o usuário')


class UpdateException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel atualizar o usuário')


class DeleteException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel deletar o usuário')
