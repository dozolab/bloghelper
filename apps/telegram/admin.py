from django.contrib import admin
from .models import TelegramUser


@admin.register(TelegramUser)
class TelegramUser(admin.ModelAdmin):
    list_display = ['user_id', 'get_full_name','is_bot']

    @staticmethod
    def get_full_name(obj):
        return f'{obj.first_name} {obj.last_name}'
# Register your models here.
