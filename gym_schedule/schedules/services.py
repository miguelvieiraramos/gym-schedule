from datetime import date

from django.core.exceptions import ValidationError

from gym_schedule.schedules.models import Schedule
from gym_schedule.schedules.selectors import find_schedule_by_date


class AddSchedule:

    def add(self, *, schedule_date: date) -> Schedule:
        has_schedule = find_schedule_by_date(schedule_date=schedule_date)
        if has_schedule:
            raise ValidationError('A schedule with that date already exists.')

        new_schedule = Schedule(date=date.today())
        new_schedule.save()

        return new_schedule


class LoadScheduleByDate:

    def load(self, *, schedule_date: date) -> Schedule:
        schedule = find_schedule_by_date(schedule_date=schedule_date)
        return schedule
