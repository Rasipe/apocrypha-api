from util.Constants import Constants


class GenreRepository:
    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, genre):
        try:
            self.cursor.execute(f'''INSERT INTO {Constants.Genre.TABLE} VALUES ({genre.description})''')
            return True
        except Exception as e:
            return False

    def delete(self, id):
        try:
            self.cursor.execute(f'DELETE FROM {Constants.Genre.TABLE} WHERE {Constants.Genre.ID} = {id}')
            return True
        except Exception as e:
            return False