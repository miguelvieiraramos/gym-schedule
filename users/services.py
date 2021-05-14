from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token

from users.models import User


def create_user(*, username: str, first_name: str, last_name: str, password: str) -> User:
    user = User(username=username, first_name=first_name, last_name=last_name)
    user.set_password(raw_password=password)
    user.save()
    return user


def create_auth_token(*, username: str, password: str) -> Token:
    user = authenticate(username=username, password=password)
    if user is None:
        raise ValidationError('Invalid credentials.')
    token, created = Token.objects.get_or_create(user=user)
    return token
