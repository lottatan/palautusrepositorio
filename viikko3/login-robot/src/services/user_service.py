from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass

import sys, pdb

class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")


        if re.match("^[a-z]+$", username) and len(username) >= 3:
            print("Ok")
        else:
            raise UserInputError("Virheellinen")

        if re.match("^(?=.*[0-9]$)(?=.*[a-zA-Z])", password) and len(password) >= 8:
            print("Ok")
        else:
            raise UserInputError("Virheellinen")

