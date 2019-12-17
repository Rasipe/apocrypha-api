from src.Exceptions.LoanExceptions import NotFoundLoanException
from src.Exceptions.UserExceptions import InvalidUserName, InvalidEmail, InvalidPhone, NotFoundException, InsertException, DeleteException, UpdateException


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        users = []
        for x in self.repository.get_all():
            user = {
                'id': x.id,
                'name': x.name,
                'phone': x.phone,
                'email': x.email,
                'loans': []
            }
            for y in x.loans:
                user['loans'].append({
                    "id": y.id,
                    "date_loan": y.date_loan,
                    'book': y.book.title
                })
            users.append(user)
        return users

    def insert(self, user):
        try:
            self.validate_user(user)
            self.repository.insert(user)
            return 'Usuário inserido com sucesso'
        except InvalidUserName as e:
            return e.args[0]
        except InvalidPhone as e:
            return e.args[0]
        except InvalidEmail as e:
            return e.args[0]
        except InsertException as e:
            return e.args[0]

    def update(self, user):
        try:
            self.validate_user(user)
            self.repository.update(user)
            return 'Usuário atualizado com sucesso'
        except InvalidUserName as e:
            return e.args[0]
        except InvalidPhone as e:
            return e.args[0]
        except InvalidEmail as e:
            return e.args[0]
        except UpdateException as e:
            return e.args[0]

    def delete(self, id):
        try:
            self.validate_id(id)
            self.repository.delete(id)
            return 'Usuário excluido com sucesso'
        except NotFoundException as e:
            return e.args[0]
        except DeleteException as e:
            return e.args[0]

    def validate_id(self, id):
        if id is None:
            raise NotFoundException

    def validate_user(self, user):
        if user.name is None:
            raise InvalidUserName
        if user.name.strip() == '':
            raise InvalidUserName
        if len(user.name) <= 3:
            raise InvalidUserName

        if user.email is None:
            raise InvalidEmail
        if user.email.strip() == '':
            raise InvalidEmail
        if len(user.email) <= 6:
            raise InvalidEmail
        if '@' not in user.email:
            raise InvalidEmail
        if '.com' not in user.email:
            raise InvalidEmail

        if user.phone is None:
            raise InvalidPhone
        if user.phone.strip() == '':
            raise InvalidPhone
        if not len(user.phone) == 11:
            raise InvalidPhone
