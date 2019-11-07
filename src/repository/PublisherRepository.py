from src.Exceptions.PublisherExceptions import InsertException, DeleteException
from src.util.Constants import Constants
from src.repository.Connection import Connection
from src.model.Publisher import Publisher


class PublisherRepository:

    def get_all(self):
        cursor = Connection.open()
        try:
            cursor.execute(f'SELECT * FROM {Constants.Publisher.TABLE}')
            publishers = []
            for x in cursor.fetchall():
                publisher = Publisher(
                    x[Constants.Publisher.ID],
                    x[Constants.Publisher.NAME],
                )
                publishers.append(publisher)
            return publishers
        finally:
            Connection.close()

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
