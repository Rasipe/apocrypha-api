class Constants:
    class Database:
        NAME = 'biblioteca'
        HOST = 'localhost'
        PASSWORD = 'Rasilpe.20000330'
        USER = 'root'

    class Publisher:
        TABLE = 'publisher'
        ID = 'publisher_id'
        NAME = 'publisher_name'

    class Collection:
        TABLE = 'collection'
        ID = 'collection_id'
        NAME = 'collection_name'

    class Genre:
        TABLE = 'genre'
        ID = 'genre_id'
        DESCRIPTION = 'genre_description'

    class Author:
        TABLE = 'author'
        ID = 'author_id'
        NAME = 'author_name'

    class Book:
        TABLE = 'book'
        ID = 'book_id'
        TITLE = 'title'
        DESCRIPTION = 'description'
        PAGES = 'pages'
        QUANTITY = 'quantity'
        VALUE_MULCT = 'value_mulct'
        PUBLISHER_ID = 'publisher_id'
        COLLECTION_ID = 'collection_id'

    class Image:
        TABLE = 'image'
        ID = 'image_id'
        CONTENT_TYPE = 'content_type'
        IMAGE = 'image'
        BOOK_ID = 'book_id'

    class AuthorBook:
        TABLE = 'author_book'
        BOOK_ID = 'book_id'
        AUTHOR_ID = 'author_id'

    class GenreBook:
        TABLE = 'book_genre'
        BOOK_ID = 'book_id'
        GENRE_ID = 'genre_id'

    class Loan:
        TABLE = 'loan'
        ID = 'loan_id'
        DATE_LOAN = 'date_loan'
        DATE_DEVOLUTION = 'date_devolution'
        BOOK_ID = 'book_id'
        USER_ID = 'user_id'

    class User:
        TABLE = 'user'
        ID = 'user_id'
        NAME = 'user_name'
        PHONE = 'phone'
        EMAIL = 'email'
