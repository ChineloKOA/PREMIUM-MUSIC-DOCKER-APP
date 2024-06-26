import string
from typing import Optional
from enum import Enum

from pydantic import EmailStr, constr, validator

from app.models.core import DateTimeModelMixin, IDModelMixin, CoreModel
from app.models.token import AccessToken


# simple check for valid username
def validate_username(username: str) -> str:
    allowed = string.ascii_letters + string.digits + "-" + "_"
    assert all(char in allowed for char in username), "Invalid characters in username."
    assert len(username) >= 3, "Username must be 3 characters or more."
    return username


class UserType(str, Enum):
    minor = "minor"
    adult = "adult"


class UserBase(CoreModel):
    """
    All common characteristics of our Users
    Leaving off password and salt from base model
    """
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    email: Optional[EmailStr]
    email_verified: bool = False
    date_of_birth: Optional[str]
    gender: Optional[str]
    user_type: Optional[UserType] = "adult"
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(CoreModel):
    """
     attributes required to create a new user - used at POST request
    """
    first_name: str
    middle_name: Optional[str]
    last_name: str
    email: EmailStr
    password: constr(min_length=7, max_length=100)
    salt: Optional[str] = None
    username: str
    date_of_birth: str
    gender: Optional[str]
    user_type: Optional[UserType]

    @validator("username", pre=True)
    def username_is_valid(cls, username: str) -> str:
        return validate_username(username)


class UserUpdate(CoreModel):
    """
    Users are allowed to update their email and/or username, gender and user type
    """
    email: Optional[EmailStr]
    username: Optional[str]
    gender: Optional[str]
    user_type: Optional[UserType]

    @validator("username", pre=True)
    def username_is_valid(cls, username: str) -> str:
        return validate_username(username)


class UserPasswordUpdate(CoreModel):
    """
    Users can change their password
    """
    password: constr(min_length=7, max_length=100)
    salt: str


class UserInDB(IDModelMixin, DateTimeModelMixin, UserBase):
    """
    Add in id, created_at, updated_at, and user's password and salt
    """
    password: constr(min_length=7, max_length=100)
    salt: str


class UserPublic(IDModelMixin, DateTimeModelMixin, UserBase):
    access_token: Optional[AccessToken]