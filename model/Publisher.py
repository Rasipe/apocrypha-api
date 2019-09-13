class Publisher:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []

    def __str__(self):
        return f'id: {self.id}\nnome: {self.name}'
