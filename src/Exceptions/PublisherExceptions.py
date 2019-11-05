class InvalidPublisherName(Exception):
    def __init__(self):
        Exception.__init__(self, 'Nome de Editora Invalido')


class DeleteException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel excluir a editora')


class InsertException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel inserir a editora')
