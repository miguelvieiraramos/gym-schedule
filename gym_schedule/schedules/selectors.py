from datetime import date

from gym_schedule.schedules.models import Schedule


def find_schedule_by_date(schedule_date: date) -> Schedule:
    try:
        return Schedule.objects.filter(date=schedule_date)
    except Schedule.DoesNotExist:
        return None
