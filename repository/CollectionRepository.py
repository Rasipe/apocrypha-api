from util.Constants import Constants


class CollectionRepository:
    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, publisher):
        try:
            self.cursor.execute(f'''INSERT INTO {Constants.Publisher.TABLE} VALUES ({publisher.name})''')
            return True
        except Exception as e:
            return False

    def delete(self, id):
        try:
            self.cursor.execute(f'DELETE FROM {Constants.Collection.TABLE} WHERE {Constants.Collection.ID} = {id}')
            return True
        except Exception as e:
            return False