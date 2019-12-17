class Genre:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.books = []
    def __str__(self):
        return f'id: {self.id}\ndescription: {self.description}'
