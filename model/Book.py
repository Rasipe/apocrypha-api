class Book:
    def __init__(self, id, title, pages, value_mulct):
        self.id = id
        self.title = title
        self.pages = pages
        self.value_mulct = value_mulct
        self.genre = {}
        self.publishers = {}
        self.collections = {}
        self.loans = []
