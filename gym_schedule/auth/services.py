from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token


class Authentication:

    def auth(*, username: str, password: str) -> Token:
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('Invalid credentials.')
        token, created = Token.objects.get_or_create(user=user)
        return token
