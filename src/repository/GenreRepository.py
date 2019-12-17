from src.Exceptions.GenreExceptions import InsertException, DeleteException
from src.util.Constants import Constants
from src.repository import Connection
from src.model.Genre import Genre


class GenreRepository:

    def get_all(self):
        cursor = Connection.open()
        try:
            cursor.execute(f'SELECT * FROM {Constants.Genre.TABLE}')
            genres = []
            for x in cursor.fetchall():
                genre = Genre(
                    x[Constants.Genre.ID],
                    x[Constants.Genre.DESCRIPTION],
                )
                genres.append(genre)
            return genres
        finally:
            Connection.close()

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
