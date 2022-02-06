from datetime import datetime, timedelta

from django.db import models


def get_expiration():
    return datetime.now() + timedelta(days=7)


class DatetimeBaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True