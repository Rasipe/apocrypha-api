from src.Exceptions.LoanExceptions import NotFoundLoanException
from src.Exceptions.UserExceptions import InvalidUserName, InvalidEmail, InvalidPhone, NotFoundException, InsertException, DeleteException, UpdateException


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get(self, id):
        try:
            self.validate_id(id)
            return self.repository.get(id)
        except NotFoundException as e:
            return e
        except NotFoundLoanException as e:
            return e

    def insert(self, user):
        try:
            self.validate_user(user)
            self.repository.insert(user)
            return 'Usuário inserido com sucesso'
        except InvalidUserName as e:
            return e
        except InvalidPhone as e:
            return e
        except InvalidEmail as e:
            return e
        except InsertException as e:
            return e

    def update(self, user):
        try:
            self.validate_user(user)
            self.repository.update(user)
            return 'Usuário atualizado com sucesso'
        except InvalidUserName as e:
            return e
        except InvalidPhone as e:
            return e
        except InvalidEmail as e:
            return e
        except UpdateException as e:
            return e

    def delete(self, id):
        try:
            self.validate_id(id)
            self.repository.delete(id)
            return 'Usuário excluido com sucesso'
        except NotFoundException as e:
            return e
        except DeleteException as e:
            return e

    def validate_id(self, id):
        if id is None:
            raise NotFoundException
        if not isinstance(id, int):
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
        if not len(user.phone) == 8:
            raise InvalidPhone
