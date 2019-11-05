from flask import Flask

from src.Controller.BookController import BookController
from src.repository.BookRepository import BookRepository
from src.repository.Connection import Connection


from src.services.BookService import BookService

Connection()
repo = BookRepository()
service = BookService(repo)

app = Flask(__name__)

controller = BookController(service, app)

app.run()