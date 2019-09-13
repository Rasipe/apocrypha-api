from model.Book import Book
from model.Publisher import Publisher
from model.Collection import Collection
from model.Loan import Loan
from model.User import User
from model.Genre import Genre


book = Book(1, 'livro', 5, 2.5)
book.publishers = Publisher(1, 'Editora')
book.collections = Collection(1, 'Coleção')
book.genre = Genre(1, 'Genero')
book.loans.append(Loan(1, '01/09/2019', '10/09/2019'))
book.loans[0].user = User(1, 'Usuário', '99999999', 'usuario@email.com')
