import bottle

from Controller import BookController
from model.Book import Book
from model.Publisher import Publisher
from model.Collection import Collection
from model.Genre import Genre
from model.Loan import Loan
from model.User import User

from repository.Connection import Connection

from services.BookService import BookService
from services.LoanService import LoanService
from services.UserService import UserService
from services.PublisherService import PublisherService

conn = Connection()

BookController.service = BookService(conn.book_repository)

bottle.debug(True)
bottle.run(host='localhost', port=8080)

conn.close_connection()
