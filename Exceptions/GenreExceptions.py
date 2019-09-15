class InvalidGenreDescription(Exception):
    def __init__(self):
        Exception.__init__(self, 'Descrição do Genero Invalido')


class DeleteException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel excluir o genero')


class InsertException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel inserir o genero')
