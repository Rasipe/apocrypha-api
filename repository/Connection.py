import sqlite3
import os


class Connection:
    def __init__(self):
        path = r'C:\sqlite\db\bibliotecaPython.db'
        file = os.path.dirname(path)
        if not os.path.exists(file):
            os.makedirs(file)
            open(path, 'w')
        self.con = sqlite3.connect(path)
        self.cur = self.con .cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS publisher(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );
        ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS collection(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );
        ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS genre(
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL
            );
        ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS book(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                pages INTEGER NOT NULL,
                value_mulct REAL NOT NULL,
                publisher_id INTEGER,
                collection_id INTEGER,
                genre_id INTEGER,
                FOREIGN KEY (publisher_id)
                    REFERENCES publisher (id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                FOREIGN KEY (collection_id)
                    REFERENCES collection (id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION,
                FOREIGN KEY (genre_id)
                    REFERENCES genre (id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
            );
        ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT
            );
        ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS loan(
                id INTEGER PRIMARY KEY,
                date_loan TEXT NOT NULL,
                date_devolution TEXT,
                book_id INTEGER,
                user_id INTEGER,
                FOREIGN KEY (book_id)
                    REFERENCES book (id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION,
                FOREIGN KEY (user_id)
                    REFERENCES user (id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
            );
        ''')
