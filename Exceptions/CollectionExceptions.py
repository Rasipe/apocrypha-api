class InvalidCollectionName(Exception):
    def __init__(self):
        Exception.__init__(self, 'Nome de Coleção Invalido')


class DeleteException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel excluir a coleção')


class InsertException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel inserir a coleção')
