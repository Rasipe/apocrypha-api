from Exceptions.GenreExceptions import InsertException, DeleteException
from util.Constants import Constants
from repository.Connection import Connection


class GenreRepository:

    def insert(self, genre):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            INSERT INTO {Constants.Genre.TABLE}(
                {Constants.Genre.DESCRIPTION}
            ) VALUES ("{genre.description}")''')
        except Exception as e:
            raise InsertException
        finally:
            cursor.close()
            Connection.close()

    def delete(self, id):
        cursor = Connection.open()
        try:
            cursor.execute(f'DELETE FROM {Constants.Genre.TABLE} WHERE {Constants.Genre.ID} = {id}')
        except Exception as e:
            raise DeleteException
        finally:
            cursor.close()
            Connection.close()
