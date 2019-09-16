from flask import Flask

from Controller.BookController import BookController
from model.Book import Book
from model.Collection import Collection
from model.Genre import Genre
from model.Publisher import Publisher
from repository.BookRepository import BookRepository
from repository.Connection import Connection


from services.BookService import BookService

Connection()
repo = BookRepository()
service = BookService(repo)

app = Flask(__name__)

controller = BookController(service, app)

app.run()
