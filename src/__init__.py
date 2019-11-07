from flask import Flask
from src.controller import BookController, GenreController, CollectionController, PublisherController, UserController, LoanController

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

app.add_url_rule('/user', view_func=UserController.get_users, methods=['GET'])
app.add_url_rule('/user', view_func=UserController.insert_user, methods=['POST'])
app.add_url_rule('/user', view_func=UserController.update_user, methods=['PUT'])
app.add_url_rule('/user/<user_id>', view_func=UserController.delete_user, methods=['DELETE'])

app.add_url_rule('/loan', view_func=LoanController.insert_loan, methods=['POST'])
app.add_url_rule('/loan/<loan_id>', view_func=LoanController.devolution, methods=['PUT'])
