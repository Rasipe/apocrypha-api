from src.Exceptions.CollectionExceptions import DeleteException, InsertException
from src.repository.Connection import Connection
from src.util.Constants import Constants


class CollectionRepository:

    def insert(self, publisher):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            INSERT INTO {Constants.Publisher.TABLE}(
                {Constants.Publisher.NAME}
            ) VALUES ("{publisher.name}")''')
        except Exception as e:
            raise InsertException
        finally:
            cursor.close()
            Connection.close()

    def delete(self, id):
        cursor = Connection.open()
        try:
            cursor.execute(f'DELETE FROM {Constants.Collection.TABLE} WHERE {Constants.Collection.ID} = {id}')
        except Exception as e:
            raise DeleteException
        finally:
            cursor.close()
            Connection.close()
