from src.repository.BookRepository import BookRepository
from src.repository.GenreRepository import GenreRepository
from src.repository.CollectionRepository import CollectionRepository
from src.repository.PublisherRepository import PublisherRepository
from src.repository.UserRepository import UserRepository
from src.repository.LoanRepository import LoanRepository


book_repository = BookRepository()
genre_repository = GenreRepository()
collection_repository = CollectionRepository()
publisher_repository = PublisherRepository()
user_repository = UserRepository()
loan_repository = LoanRepository()
