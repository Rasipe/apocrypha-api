from Exceptions.PublisherExceptions import InsertException, DeleteException
from util.Constants import Constants
from repository.Connection import Connection


class PublisherRepository:

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
            cursor.execute(f'DELETE FROM {Constants.Publisher.TABLE} WHERE {Constants.Publisher.ID} = {id}')
        except Exception as e:
            raise DeleteException
        finally:
            cursor.close()
            Connection.close()
