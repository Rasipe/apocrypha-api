class InvalidBookTitle(Exception):
    def __init__(self):
        Exception.__init__(self, 'Titulo Inválido')


class InvalidPublisher(Exception):
    def __init__(self):
        Exception.__init__(self, 'Editora Inválida')


class InvalidGenre(Exception):
    def __init__(self):
        Exception.__init__(self, 'Genero Inválido')


class NotFoundException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Livro não encontrado')


class InsertException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel inserir o livro')


class UpdateException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel atualizar o livro')


class DeleteException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel deletar o livro')
