from datetime import date


from gym_schedule.schedules.models import Schedule
from gym_schedule.schedules.selectors import find_schedule_by_date


def get_or_create_schedule(schedule_date: date) -> Schedule:
    has_schedule = find_schedule_by_date(schedule_date=schedule_date)
    if has_schedule:
        return has_schedule

    new_schedule = Schedule(date=date.today())
    new_schedule.save()

    return new_schedule
