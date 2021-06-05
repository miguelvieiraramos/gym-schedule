import datetime
from django.core.exceptions import ValidationError

from gym_schedule.times.models import Time


class AddTime:
    ALLOWED_MINUTES = (30,)

    def add(self, *, hour: int, minute: int) -> Time:
        if minute not in AddTime.ALLOWED_MINUTES:
            raise ValidationError(f'{minute} is not allowed as a minute.')

        time = datetime.time(hour, minute)
        has_time = Time.objects.filter(time=time).exists()

        if has_time:
            raise ValidationError('This time already exists.')

        new_time = Time.objects.create(is_active=True, time=time)
        return new_time
