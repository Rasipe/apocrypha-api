from Exceptions.PublisherExceptions import InvalidPublisherName, InvalidId


class PublisherService:
    def __init__(self, repository):
        self.repository = repository

    def insert(self, publisher):
        try:
            self.validate(publisher)
            self.repository.insert(publisher)
            return 'Editora Inserida com sucesso'
        except InvalidPublisherName as e:
            return e

    def delete(self, id):
        try:
            if id is None:
                raise InvalidId
            if not isinstance(id, int):
                raise InvalidId
            self.repository.delete(id)
            return 'Editora deletado com sucesso'
        except InvalidId as e:
            return e

    def validate(self, publisher):
        if publisher.name is None:
            raise InvalidPublisherName
        if publisher.name.strip() == '':
            raise InvalidPublisherName
        if len(publisher.name) <= 3:
            raise InvalidPublisherName
