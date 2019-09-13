class Book:
    def __init__(self, id, title, pages, value_mulct):
        self.id = id
        self.title = title
        self.pages = pages
        self.value_mulct = value_mulct
        self.genre = {}
        self.publisher = {}
        self.collection = {}
        self.loans = []

    def __str__(self):
        s = f'id: {self.id}' \
               f'\ntitle: {self.title}' \
               f'\npaginas: {self.pages}' \
               f'\nValor da Multa: {self.value_mulct}' \
               f'\nGenero: \n{self.genre}' \
               f'\nEditora: \n{self.publisher}' \
               f'\nColeção: \n{self.collection}'
        for loan in self.loans:
            s.join(f'\n{loan}')
        return s
