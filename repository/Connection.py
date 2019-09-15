from injector import Module, Key, provider, Injector, inject, singleton
import sqlite3
import os

from Exceptions.ConnectionExceptions import ConnectionException
from util.Constants import Constants

connection = {}


class Connection:
    @inject
    def __init__(self):
        cursor = Connection.open()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Publisher.TABLE}(
                {Constants.Publisher.ID} INTEGER PRIMARY KEY AUTOINCREMENT,
                {Constants.Publisher.NAME} TEXT NOT NULL
            );
        ''')
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Collection.TABLE}(
                {Constants.Collection.ID} INTEGER PRIMARY KEY AUTOINCREMENT,
                {Constants.Collection.NAME} TEXT NOT NULL
            );
        ''')
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Genre.TABLE}(
                {Constants.Genre.ID} INTEGER PRIMARY KEY AUTOINCREMENT,
                {Constants.Genre.DESCRIPTION} TEXT NOT NULL
            );
        ''')
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Book.TABLE}(
                {Constants.Book.ID} INTEGER PRIMARY KEY AUTOINCREMENT,
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
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.User.TABLE}(
                {Constants.User.ID} INTEGER PRIMARY KEY AUTOINCREMENT,
                {Constants.User.NAME} TEXT NOT NULL,
                {Constants.User.PHONE} TEXT,
                {Constants.User.EMAIL} TEXT
            );
        ''')
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {Constants.Loan.TABLE}(
                {Constants.Loan.ID} INTEGER PRIMARY KEY AUTOINCREMENT,
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
        cursor.execute(f'''INSERT INTO {Constants.Publisher.TABLE} VALUES (1, "Editora 1")''')
        cursor.execute(f'''INSERT INTO {Constants.Publisher.TABLE} VALUES (2, "Editora 2")''')

        cursor.execute(f'''INSERT INTO {Constants.Collection.TABLE} VALUES (1, "Coleção 1")''')
        cursor.execute(f'''INSERT INTO {Constants.Collection.TABLE} VALUES (2, "Coleção 2")''')

        cursor.execute(f'''INSERT INTO {Constants.Genre.TABLE} VALUES (1, "Genero 1")''')
        cursor.execute(f'''INSERT INTO {Constants.Genre.TABLE} VALUES (2, "Genero 2")''')

        cursor.execute(f'''INSERT INTO {Constants.User.TABLE} VALUES (1, "Usuario 1", "99999999", "user@email.com")''')
        cursor.execute(f'''INSERT INTO {Constants.User.TABLE} VALUES (2, "Usuario 2", "99999999", "user@email.com")''')

        cursor.execute(f'''INSERT INTO {Constants.Loan.TABLE} VALUES (1, "01/09/2019", "", 1, 1)''')
        cursor.execute(f'''INSERT INTO {Constants.Loan.TABLE} VALUES (2, "01/08/2019", "15/08/2019", 1, 2)''')

        cursor.execute(f'SELECT * FROM {Constants.Book.TABLE}')

        cursor.close()
        Connection.close()

    @staticmethod
    def open():
        try:
            path = r'C:\sqlite\db\bibliotecaPython.db'
            file = os.path.dirname(path)
            if not os.path.exists(file):
                os.makedirs(file)
                open(path, 'w')
            global connection
            if connection == {}:
                connection = sqlite3.connect(path)
                connection.row_factory = sqlite3.Row
            return connection.cursor()
        except Exception as e:
            raise ConnectionException

    @staticmethod
    def close(close=False):
        global connection
        if close:
            connection.close()
