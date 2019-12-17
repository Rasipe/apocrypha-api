
from src.Exceptions.BookExceptions import NotFoundException, InsertException, DeleteException, UpdateException
from src.repository import Connection
from src.util.Constants import Constants

from src.model.Book import Book
from src.model.Genre import Genre
from src.model.Collection import Collection
from src.model.Publisher import Publisher


class BookRepository:
    def get_all(self):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
                SELECT * FROM {Constants.Book.TABLE}
                LEFT JOIN {Constants.Collection.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.COLLECTION_ID} = {Constants.Collection.TABLE}.{Constants.Collection.ID}
                LEFT JOIN {Constants.Publisher.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.PUBLISHER_ID} = {Constants.Publisher.TABLE}.{Constants.Publisher.ID}
                LEFT JOIN {Constants.Image.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.ID} = {Constants.Image.TABLE}.{Constants.Image.BOOK_ID}
                LEFT JOIN {Constants.AuthorBook.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.ID} = {Constants.AuthorBook.TABLE}.{Constants.AuthorBook.BOOK_ID}
                LEFT JOIN {Constants.Author.TABLE}
                    ON {Constants.Author.TABLE}.{Constants.Author.ID} = {Constants.AuthorBook.TABLE}.{Constants.AuthorBook.AUTHOR_ID}
                LEFT JOIN {Constants.GenreBook.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.ID} = {Constants.GenreBook.TABLE}.{Constants.GenreBook.BOOK_ID}
                LEFT JOIN {Constants.Genre.TABLE}
                    ON {Constants.Genre.TABLE}.{Constants.Genre.ID} = {Constants.GenreBook.TABLE}.{Constants.GenreBook.GENRE_ID}
            ''')
            return cursor.fetchall()
        finally:
            Connection.close()

    def get(self, book_id):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
                SELECT * FROM {Constants.Book.TABLE}
                LEFT JOIN {Constants.Collection.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.COLLECTION_ID} = {Constants.Collection.TABLE}.{Constants.Collection.ID}
                LEFT JOIN {Constants.Publisher.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.PUBLISHER_ID} = {Constants.Publisher.TABLE}.{Constants.Publisher.ID}
                LEFT JOIN {Constants.Image.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.ID} = {Constants.Image.TABLE}.{Constants.Image.BOOK_ID}
                LEFT JOIN {Constants.AuthorBook.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.ID} = {Constants.AuthorBook.TABLE}.{Constants.AuthorBook.BOOK_ID}
                LEFT JOIN {Constants.Author.TABLE}
                    ON {Constants.Author.TABLE}.{Constants.Author.ID} = {Constants.AuthorBook.TABLE}.{Constants.AuthorBook.AUTHOR_ID}
                LEFT JOIN {Constants.GenreBook.TABLE}
                    ON {Constants.Book.TABLE}.{Constants.Book.ID} = {Constants.GenreBook.TABLE}.{Constants.GenreBook.BOOK_ID}
                LEFT JOIN {Constants.Genre.TABLE}
                    ON {Constants.Genre.TABLE}.{Constants.Genre.ID} = {Constants.GenreBook.TABLE}.{Constants.GenreBook.GENRE_ID}
                WHERE {Constants.Book.TABLE}.{Constants.Book.ID} = {book_id};
            ''')
            return cursor.fetchall()
        finally:
            Connection.close()

    def get_count_loans(self, book_id):
        cursor = Connection.open()
        try:
            cursor.execute(f'''SELECT COUNT({Constants.Loan.TABLE}.{Constants.Loan.ID}) AS loans
                           FROM {Constants.Loan.TABLE}
                           WHERE {Constants.Loan.TABLE}.{Constants.Loan.BOOK_ID} = {book_id};
            ''')
            return cursor.fetchall()[0]['loans']
        finally:
            Connection.close()

    def insert(self, book):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            INSERT INTO {Constants.Book.TABLE} (
                {Constants.Book.TITLE},
                {Constants.Book.DESCRIPTION},
                {Constants.Book.QUANTITY},
                {Constants.Book.PAGES},
                {Constants.Book.VALUE_MULCT},
                {Constants.Book.PUBLISHER_ID},
                {Constants.Book.COLLECTION_ID}
            ) VALUES(
                "{book['Title']}",
                "{book['Description']}",
                {book['Quantity']},
                {book['Pages']},
                {book['ValueMulct']},
                {book['Publisher']},
                {book['Collection']}
            );
            ''')

            cursor.execute(f'SELECT LAST_INSERT_ID()')
            book_id = cursor.fetchall()[0]['LAST_INSERT_ID()']

            for author in book['Authors']:
                cursor.execute(f'''
                    INSERT INTO {Constants.AuthorBook.TABLE}
                    VALUES ({book_id},{author})
                ''')
            for genre in book['Genres']:
                cursor.execute(f'''
                    INSERT INTO {Constants.GenreBook.TABLE}
                    VALUES ({book_id},{genre})
                ''')
            for image in book['Images']:
                cursor.execute(f'''
                    INSERT INTO {Constants.Image.TABLE} (
                        {Constants.Image.CONTENT_TYPE},
                        {Constants.Image.IMAGE},
                        {Constants.Image.BOOK_ID}
                    ) VALUES (
                        "{image['ContentType']}",
                        "{image['Image']}",
                        {book_id}
                    )
                ''')
            return 'Livro Inserido com Sucesso'
        except Exception as e:
            raise InsertException
        finally:
            Connection.close()

    def update(self, book):
        cursor = Connection.open()
        try:
            cursor.execute(f'''
            UPDATE {Constants.Book.TABLE}
            SET {Constants.Book.TITLE} = "{book['Title']}",
                {Constants.Book.DESCRIPTION} = "{book['Description']}",
                {Constants.Book.QUANTITY} = {book['Quantity']},
                {Constants.Book.PAGES} = {book['Pages']},
                {Constants.Book.VALUE_MULCT} = {book['ValueMulct']},
                {Constants.Book.PUBLISHER_ID} = {book['Publisher']},
                {Constants.Book.COLLECTION_ID} = {book['Collection']}
            WHERE {Constants.Book.ID} = {book['Id']}
            ''')

            cursor.execute(f'''
                SELECT {Constants.Image.ID}
                FROM {Constants.Image.TABLE}
                WHERE {Constants.Image.BOOK_ID} = {book['Id']};
            ''')
            db_images = []
            for image in cursor.fetchall():
                db_images.append(image[Constants.Image.ID])
            for image in book['Images']:
                if 'Id' not in image:
                    cursor.execute(f'''
                        INSERT INTO {Constants.Image.TABLE} (
                            {Constants.Image.CONTENT_TYPE},
                            {Constants.Image.IMAGE},
                            {Constants.Image.BOOK_ID}
                        ) VALUES (
                            "{image['ContentType']}",
                            "{image['Image']}",
                            {book['Id']}
                        );
                    ''')
            for db_image in db_images:
                if db_image not in book['Images']:
                    cursor.execute(f'DELETE FROM {Constants.Image.TABLE} WHERE {Constants.Image.ID} = {db_image}')

            cursor.execute(f'''
                SELECT * FROM {Constants.AuthorBook.TABLE}
                WHERE {Constants.AuthorBook.BOOK_ID} = {book['Id']};
            ''')
            db_genres = []
            for genre in cursor.fetchall():
                db_genres.append(genre[Constants.AuthorBook.AUTHOR_ID])
            for genre in book['Authors']:
                if genre not in db_genres:
                    cursor.execute(f'''
                    INSERT INTO {Constants.AuthorBook.TABLE}
                    VALUES ({book['Id']},{genre})
                    ''')
            for db_genre in db_genres:
                if db_genre not in book['Authors']:
                    cursor.execute(f'''
                        DELETE FROM {Constants.AuthorBook.TABLE}
                        WHERE {Constants.AuthorBook.AUTHOR_ID} = {db_genre}
                            AND {Constants.AuthorBook.BOOK_ID} = {book['Id']}
                    ''')

            cursor.execute(f'''
                            SELECT * FROM {Constants.GenreBook.TABLE}
                            WHERE {Constants.GenreBook.BOOK_ID} = {book['Id']};
                        ''')
            db_genres = []
            for genre in cursor.fetchall():
                db_genres.append(genre[Constants.GenreBook.GENRE_ID])
            for genre in book['Genres']:
                if genre not in db_genres:
                    cursor.execute(f'''
                        INSERT INTO {Constants.GenreBook.TABLE}
                        VALUES ({book['Id']},{genre})
                    ''')
            for db_genre in db_genres:
                if db_genre not in book['Genres']:
                    cursor.execute(f'''
                        DELETE FROM {Constants.GenreBook.TABLE}
                        WHERE {Constants.GenreBook.GENRE_ID} = {db_genre}
                            AND {Constants.GenreBook.BOOK_ID} = {book['Id']}
                    ''')
            return 'Livro alterado com sucesso'
        except Exception as e:
            raise UpdateException
        finally:
            Connection.close()

    def delete(self, id):
        cursor = Connection.open()
        try:
            cursor.execute(f'DELETE FROM {Constants.GenreBook.TABLE} WHERE {Constants.GenreBook.BOOK_ID} = {id}')
            cursor.execute(f'DELETE FROM {Constants.AuthorBook.TABLE} WHERE {Constants.AuthorBook.BOOK_ID} = {id}')
            cursor.execute(f'DELETE FROM {Constants.Image.TABLE} WHERE {Constants.Image.BOOK_ID} = {id}')
            cursor.execute(f'DELETE FROM {Constants.Book.TABLE} WHERE {Constants.Book.ID} = {id}')
            return 'Libro Excluido com sucesso'
        except Exception as e:
            raise DeleteException
        finally:
            Connection.close()


book_repository = BookRepository()
