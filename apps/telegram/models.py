from django.db import models

# project
from apps.shared.models import TimeStampedModel
from apps.telegram import steps


class TelegramUser(TimeStampedModel):
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    language_code = models.CharField(max_length=10, null=True)
    is_bot=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



