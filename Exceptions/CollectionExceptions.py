class InvalidCollectionName(Exception):
    def __init__(self):
        Exception.__init__(self, 'Nome de Coleção Invalido')

class InvalidId(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel excluir a coleção')
