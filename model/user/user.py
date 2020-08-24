import uuid
# from dataclasses import dataclass, field
from typing import Dict, List

from model.model import Model
from common.database import Database
from common.utils import Utils
# import model.user.errors as UserErrors
# from model.user import UserErrors
from model.user.errors import UserError, UserNotFoundError, IncorrectPasswordError, InvalidEmailError,\
    UserAlreadyRegisteredError


# @dataclass
class User(Model):

    collection = "users"
#    collection: str = field(init=False, default="users")
#    email: str
#    password: str
#    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __init__(self, email: str, password: str, _id: str = None):
        super().__init__()
        self.email = email
        self.password = password
        self._id = _id or uuid.uuid4().hex

    @classmethod
    def find_by_email(cls, email: str) -> "User":
        try:
            return cls.find_one_by('email', email)
        except TypeError:
            raise UserNotFoundError('A user with this e-mail was not found.')  # UserErrors.

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:

        user = cls.find_by_email(email)

        if not Utils.check_hashed_password(password, user.password):
            # Tell the user that their password is wrong
            raise IncorrectPasswordError("Your password was wrong.")  # UserErrors.

        return True

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:

        if not Utils.email_is_valid(email):
            raise InvalidEmailError("The e-mail does not have the right format.")  # UserErrors.

        try:
            user = cls.find_by_email(email)
            raise UserAlreadyRegisteredError("The e-mail you used to register already exists.")  # UserErrors.U
        except UserNotFoundError:  # UserErrors.U
            User(email, Utils.hash_password(password)).save_to_mongo()

        return True

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }