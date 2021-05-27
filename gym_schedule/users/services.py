from django.core.exceptions import ValidationError

from gym_schedule.users.models import User


class AddUser:

    def add(self, *, username: str, first_name: str, last_name: str, password: str) -> User:
        user = User(username=username, first_name=first_name, last_name=last_name)
        user.set_password(raw_password=password)
        user.save()

        return user


class LoadUserById:

    def load(self, *, id: int, current_user: User) -> User:
        if current_user.id != id and not current_user.is_superuser:
            raise ValidationError('You have no permission to get this user.')

        user = User.objects.filter(id=id).first()

        if user is None:
            raise ValidationError('User not found.')

        return user


class LoadUsers:

    def load(self, *, current_user: User):
        if not current_user.is_superuser:
            raise ValidationError('You do not have permission to perform this action.')

        users = User.objects.all()

        return users
