class InvalidBookTitle(Exception):
    def __init__(self):
        Exception.__init__(self, 'Titulo Inválido')


class InvalidPublisher(Exception):
    def __init__(self):
        Exception.__init__(self, 'Editora Inválida')


class InvalidGenre(Exception):
    def __init__(self):
        Exception.__init__(self, 'Genero Inválido')


class InvalidId(Exception):
    def __init__(self):
        Exception.__init__(self, 'Livro não encontrado')
