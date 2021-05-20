import uuid

from django.db import models


class Schedule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    date = models.DateField(unique=True)
