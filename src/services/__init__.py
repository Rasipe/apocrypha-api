from src.repository import book_repository, genre_repository, collection_repository, publisher_repository, user_repository, loan_repository
from src.services.BookService import BookService
from src.services.GenreService import GenreService
from src.services.CollectionService import CollectionService
from src.services.PublisherService import PublisherService
from src.services.UserService import UserService
from src.services.LoanService import LoanService

book_service = BookService(book_repository)
genre_service = GenreService(genre_repository)
collection_service = CollectionService(collection_repository)
publisher_service = PublisherService(publisher_repository)
user_service = UserService(user_repository)
loan_service = LoanService(loan_repository)
