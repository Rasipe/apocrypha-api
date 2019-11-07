from flask import Flask
from src.controller import BookController, GenreController, CollectionController,PublisherController

app = Flask(__name__)

app.add_url_rule('/book/<book_id>', view_func=BookController.get_book, methods=['GET'])
app.add_url_rule('/book', view_func=BookController.get_books, methods=['GET'])
app.add_url_rule('/book', view_func=BookController.insert_book, methods=['POST'])
app.add_url_rule('/book', view_func=BookController.update_book, methods=['PUT'])
app.add_url_rule('/book/<book_id>', view_func=BookController.delete_book, methods=['DELETE'])

app.add_url_rule('/genre', view_func=GenreController.get_genres, methods=['GET'])
app.add_url_rule('/genre', view_func=GenreController.insert_genre, methods=['POST'])

app.add_url_rule('/collection', view_func=CollectionController.get_collections, methods=['GET'])
app.add_url_rule('/collection', view_func=CollectionController.insert_collection, methods=['POST'])

app.add_url_rule('/publisher', view_func=PublisherController.get_publishers, methods=['GET'])
app.add_url_rule('/publisher', view_func=PublisherController.insert_publisher, methods=['POST'])
