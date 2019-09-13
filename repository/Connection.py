import sqlite3
import os

from repository.BookRepository import BookRepository
from repository.UserRepository import UserRepository

from util.Constants import Constants


class Connection:
    def __init__(self):
        path = r'C:\sqlite\db\bibliotecaPython.db'
        file = os.path.dirname(path)
        if not os.path.exists(file):
            os.makedirs(file)
            open(path, 'w')
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection .cursor()
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Publisher.TABLE}(
                {Constants.Publisher.ID} INTEGER PRIMARY KEY,
                {Constants.Publisher.NAME} TEXT NOT NULL
            );
        ''')
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Collection.TABLE}(
                {Constants.Collection.ID} INTEGER PRIMARY KEY,
                {Constants.Collection.NAME} TEXT NOT NULL
            );
        ''')
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Genre.TABLE}(
                {Constants.Genre.ID} INTEGER PRIMARY KEY,
                {Constants.Genre.DESCRIPTION} TEXT NOT NULL
            );
        ''')
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Book.TABLE}(
                {Constants.Book.ID} INTEGER PRIMARY KEY,
                {Constants.Book.TITLE} TEXT NOT NULL,
                {Constants.Book.PAGES} INTEGER NOT NULL,
                {Constants.Book.VALUE_MULCT} REAL NOT NULL,
                {Constants.Book.PUBLISHER_ID} INTEGER,
                {Constants.Book.COLLECTION_ID} INTEGER,
                {Constants.Book.GENRE_ID} INTEGER,
                FOREIGN KEY ({Constants.Book.PUBLISHER_ID})
                    REFERENCES {Constants.Publisher.TABLE} ({Constants.Publisher.ID})
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                FOREIGN KEY ( {Constants.Book.COLLECTION_ID})
                    REFERENCES {Constants.Collection.TABLE} ({Constants.Collection.ID})
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION,
                FOREIGN KEY ({Constants.Book.GENRE_ID})
                    REFERENCES {Constants.Genre.TABLE} ({Constants.Genre.ID})
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
            );
        ''')
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.User.TABLE}(
                {Constants.User.ID} INTEGER PRIMARY KEY,
                {Constants.User.NAME} TEXT NOT NULL,
                {Constants.User.PHONE} TEXT,
                {Constants.User.EMAIL} TEXT
            );
        ''')
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Loan.TABLE}(
                {Constants.Loan.ID} INTEGER PRIMARY KEY,
                {Constants.Loan.DATE_LOAN} TEXT NOT NULL,
                {Constants.Loan.DATE_DEVOLUTION} TEXT,
                {Constants.Loan.BOOK_ID} INTEGER,
                {Constants.Loan.USER_ID} INTEGER,
                FOREIGN KEY ({Constants.Loan.BOOK_ID})
                    REFERENCES {Constants.Book.TABLE} ({Constants.Book.ID})
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION,
                FOREIGN KEY ({Constants.Loan.USER_ID})
                    REFERENCES {Constants.User.TABLE} ({Constants.User.ID})
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
            );
        ''')
        self.cursor.execute(f'''INSERT INTO {Constants.Publisher.TABLE} VALUES (1, "Editora 1")''')
        self.cursor.execute(f'''INSERT INTO {Constants.Publisher.TABLE} VALUES (2, "Editora 2")''')

        self.cursor.execute(f'''INSERT INTO {Constants.Collection.TABLE} VALUES (1, "Coleção 1")''')
        self.cursor.execute(f'''INSERT INTO {Constants.Collection.TABLE} VALUES (2, "Coleção 2")''')

        self.cursor.execute(f'''INSERT INTO {Constants.Genre.TABLE} VALUES (1, "Genero 1")''')
        self.cursor.execute(f'''INSERT INTO {Constants.Genre.TABLE} VALUES (2, "Genero 2")''')

        self.cursor.execute(f'''INSERT INTO {Constants.User.TABLE} VALUES (1, "Usuario 1", "99999999", "user@email.com")''')
        self.cursor.execute(f'''INSERT INTO {Constants.User.TABLE} VALUES (2, "Usuario 2", "99999999", "user@email.com")''')

        self.cursor.execute(f'''INSERT INTO {Constants.Loan.TABLE} VALUES (1, "01/09/2019", "", 1, 1)''')
        self.cursor.execute(f'''INSERT INTO {Constants.Loan.TABLE} VALUES (2, "01/08/2019", "15/08/2019", 1, 2)''')

        self.book_repository = BookRepository(self.cursor)
        self.user_repository = UserRepository(self.cursor)

    def close_connection(self):
        self.cursor.close()
        self.book_repository.cursor.close()
        self.user_repository.cursor.close()
        self.connection.close()
