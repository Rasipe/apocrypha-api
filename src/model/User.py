class User:
    def __init__(self, id, name, phone='', email=''):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.loans = []

    def __str__(self):
        return f'Id: {self.id}' \
               f'\nNome: {self.name}' \
               f'\nPhone: {self.phone}' \
               f'\nemail: {self.email}'
