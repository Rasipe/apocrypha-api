from src.Exceptions.CollectionExceptions import InvalidCollectionName, DeleteException, InsertException


class CollectionService:
    def __init__(self, repository):
        self.repository = repository

    def insert(self, collection):
        try:
            self.validate(collection)
            self.repository.insert(collection)
            return 'Coleção Inserida com sucesso'
        except InvalidCollectionName as e:
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
            return 'Coleção deletada com sucesso'
        except DeleteException as e:
            return e

    def validate(self, collection):
        if collection.name is None:
            raise InvalidCollectionName
        if collection.name.strip() == '':
            raise InvalidCollectionName
        if len(collection.name) <= 3:
            raise InvalidCollectionName
