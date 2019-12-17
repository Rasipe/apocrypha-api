from mysql import connector

from src.util.Constants import Constants


connection = {}


def create_database():
    global connection
    create_database_if_not_exist()

    cursor = open()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.Publisher.TABLE}(
            {Constants.Publisher.ID} INT AUTO_INCREMENT PRIMARY KEY,
            {Constants.Publisher.NAME} VARCHAR(25) NOT NULL
        );
    ''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.Collection.TABLE}(
            {Constants.Collection.ID} INT AUTO_INCREMENT PRIMARY KEY,
            {Constants.Collection.NAME} VARCHAR(50) NOT NULL
        );
    ''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.Genre.TABLE}(
            {Constants.Genre.ID} INT AUTO_INCREMENT PRIMARY KEY,
            {Constants.Genre.DESCRIPTION} VARCHAR(25) NOT NULL
        );
    ''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.Author.TABLE}(
            {Constants.Author.ID} INT AUTO_INCREMENT PRIMARY KEY,
            {Constants.Author.NAME} VARCHAR(50) NOT NULL
        );
    ''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.Book.TABLE}(
            {Constants.Book.ID} INT AUTO_INCREMENT PRIMARY KEY,
            {Constants.Book.TITLE} VARCHAR(100) NOT NULL,
            {Constants.Book.DESCRIPTION} VARCHAR(5000) NOT NULL,
            {Constants.Book.QUANTITY} INT DEFAULT 1,
            {Constants.Book.PAGES} INT NOT NULL,
            {Constants.Book.VALUE_MULCT} FLOAT NOT NULL,
            {Constants.Book.PUBLISHER_ID} INT,
            {Constants.Book.COLLECTION_ID} INT,
            FOREIGN KEY ({Constants.Book.PUBLISHER_ID})
                REFERENCES {Constants.Publisher.TABLE} ({Constants.Publisher.ID}),
            FOREIGN KEY ( {Constants.Book.COLLECTION_ID})
                REFERENCES {Constants.Collection.TABLE} ({Constants.Collection.ID})
        );
    ''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.Image.TABLE}(
            {Constants.Image.ID} INT AUTO_INCREMENT PRIMARY KEY,
            {Constants.Image.CONTENT_TYPE} VARCHAR(45),
            {Constants.Image.IMAGE} LONGBLOB,
            {Constants.Image.BOOK_ID} INT,
            FOREIGN KEY ({Constants.Image.BOOK_ID})
                REFERENCES {Constants.Book.TABLE} ({Constants.Book.ID})
        );
    ''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.GenreBook.TABLE}(
            {Constants.GenreBook.BOOK_ID} INT,
            {Constants.GenreBook.GENRE_ID} INT,
            PRIMARY KEY ({Constants.GenreBook.GENRE_ID}, {Constants.GenreBook.BOOK_ID})
        );
    ''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.AuthorBook.TABLE}(
            {Constants.AuthorBook.BOOK_ID} INT,
            {Constants.AuthorBook.AUTHOR_ID} INT,
            PRIMARY KEY ({Constants.AuthorBook.AUTHOR_ID}, {Constants.AuthorBook.BOOK_ID})
        );
    ''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.User.TABLE}(
            {Constants.User.ID} INT AUTO_INCREMENT PRIMARY KEY,
            {Constants.User.NAME} VARCHAR(25) NOT NULL,
            {Constants.User.PHONE} VARCHAR(25),
            {Constants.User.EMAIL} VARCHAR(50)
        );
    ''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {Constants.Loan.TABLE}(
            {Constants.Loan.ID} INT AUTO_INCREMENT PRIMARY KEY,
            {Constants.Loan.DATE_LOAN} VARCHAR(50) NOT NULL,
            {Constants.Loan.DATE_DEVOLUTION} VARCHAR(50),
            {Constants.Loan.BOOK_ID} INT,
            {Constants.Loan.USER_ID} INT,
            FOREIGN KEY ({Constants.Loan.BOOK_ID})
                REFERENCES {Constants.Book.TABLE} ({Constants.Book.ID}),
            FOREIGN KEY ({Constants.Loan.USER_ID})
                REFERENCES {Constants.User.TABLE} ({Constants.User.ID})
        );
    ''')
    close()


def open():
    global connection
    connection = connector.connect(
        host=Constants.Database.HOST,
        user=Constants.Database.USER,
        password=Constants.Database.PASSWORD,
        database=Constants.Database.NAME,
    )
    connection.autocommit = True
    return connection.cursor(dictionary=True)


def close():
    global connection
    connection.close()


def create_database_if_not_exist():
    conn = connector.connect(
        host=Constants.Database.HOST,
        user=Constants.Database.USER,
        password=Constants.Database.PASSWORD
    )
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        if Constants.Database.NAME in x:
            conn.close()
            return
    cursor.execute(f'CREATE DATABASE {Constants.Database.NAME}')
    conn.close()
