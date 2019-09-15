from injector import Module, Key, provider, Injector, inject, singleton

from model.Book import Book
from model.Collection import Collection
from model.Genre import Genre
from model.Publisher import Publisher
from repository.BookRepository import BookRepository
from repository.Connection import Connection

# injector = Injector()
# injector.get(Connection)

# test = injector.get(BookRepository)
from services.BookService import BookService

Connection()
repo = BookRepository()
service = BookService(repo)

book = Book(1, 'teste', 250, 2.5)
book.publisher = Publisher(0, '')
book.collection = Collection(0, '')
book.genre = Genre(0, '')
print(service.insert(book))

print(service.get_all())
