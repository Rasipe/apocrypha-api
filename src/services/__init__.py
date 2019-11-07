from src.repository import book_repository
from src.services.BookService import BookService

from src.repository import genre_repository
from src.services.GenreService import GenreService

from src.repository import collection_repository
from src.services.CollectionService import CollectionService

from src.repository import publisher_repository
from src.services.PublisherService import PublisherService

book_service = BookService(book_repository)
genre_service = GenreService(genre_repository)
collection_service = CollectionService(collection_repository)
publisher_service = PublisherService(publisher_repository)
