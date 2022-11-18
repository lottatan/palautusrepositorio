from entities.user import User
import re
from repositories.user_repository import (
    user_repository as default_user_repository
)

class UserInputError(Exception):
    pass

class AuthenticationError(Exception):
    pass

class NonExistentError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user:
            raise NonExistentError("Invalid username or password")
        
        if user and user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise Exception("Username and password are required")

        if re.match("^[a-z]+$", username) and len(username) >= 3:
            print("Ok")
        else:
            raise Exception("Virheellinen käyttäjätunnus")


        if re.match("^(?=.*[0-9]$)(?=.*[a-zA-Z])", password) and len(password) >= 8:
            print("Ok")
        else:
            raise Exception("Virheellinen salasana")
        
        if not password_confirmation or password != password_confirmation:
            raise Exception("Passwords don't match")
        

user_service = UserService()
