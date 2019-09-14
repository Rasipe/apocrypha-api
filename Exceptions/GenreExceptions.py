class InvalidGenreDescription(Exception):
    def __init__(self):
        Exception.__init__(self, 'Descrição do Genero Invalido')


class InvalidId(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel excluir o genero')
