from django.db import models


class Time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    time = models.TimeField()

    class Meta:
        unique_together = ['hour', 'minute']
