from src.Exceptions.CollectionExceptions import DeleteException, InsertException
from src.repository import Connection
from src.util.Constants import Constants
from src.model.Collection import Collection


class CollectionRepository:

    def get_all(self):
        cursor = Connection.open()
        try:
            cursor.execute(f'SELECT * FROM {Constants.Collection.TABLE}')
            collections = []
            for x in cursor.fetchall():
                collection = Collection(
                    x[Constants.Collection.ID],
                    x[Constants.Collection.NAME],
                )
                collections.append(collection)
            return collections
        finally:
            Connection.close()

    def insert(self, collection):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            INSERT INTO {Constants.Collection.TABLE}(
                {Constants.Collection.NAME}
            ) VALUES ("{collection.name}")''')
        except Exception as e:
            raise InsertException
        finally:
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
