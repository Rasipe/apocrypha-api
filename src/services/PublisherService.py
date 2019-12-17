from src.Exceptions.PublisherExceptions import InvalidPublisherName, DeleteException, InsertException


class PublisherService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        publishers = []
        for x in self.repository.get_all():
            publishers.append({
                'value': x.id,
                'label': x.name
            })
        return publishers

    def insert(self, publisher):
        try:
            self.validate(publisher)
            self.repository.insert(publisher)
            return 'Editora Inserida com sucesso'
        except InvalidPublisherName as e:
            return e
        except InsertException as e:
            return e

    def delete(self, id):
        try:
            if id is None:
                raise DeleteException
            if not isinstance(id, int):
                raise DeleteException
            self.repository.delete(id)
            return 'Editora deletado com sucesso'
        except DeleteException as e:
            return e

    def validate(self, publisher):
        if publisher.name is None:
            raise InvalidPublisherName
        if publisher.name.strip() == '':
            raise InvalidPublisherName
        if len(publisher.name) <= 3:
            raise InvalidPublisherName
