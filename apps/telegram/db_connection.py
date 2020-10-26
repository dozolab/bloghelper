from apps.telegram.models import TelegramUser
from apps.telegram import steps


# gets
def get_user_step(user_id):
    try:
        user = TelegramUser.objects.get(user_id=user_id)
        if user.step:
            return user.step
        return steps.DEFAULT
    except TelegramUser.DoesNotExist:
        return steps.DEFAULT


def get_user_from_db(message):
    try:
        user = TelegramUser.objects.get(user_id=message.from_user.id)
        user.__setattr__('is_new', False)
    except TelegramUser.DoesNotExist:
        print(message)
        user = TelegramUser.objects.create(user_id=message.from_user.id, is_bot=message.from_user.is_bot, first_name=message.from_user.first_name, last_name=message.from_user.last_name)
        user.__setattr__('is_new', True)
        return user
    return user


# def get_user_lang(user_id):
#     return get_user_from_db(user_id).lang
#
#
# def get_languages():
#     return TelegramUser().get_languages()


# updates
def update_user_model(user_id, **kwargs):
    """
        update fields need fields name from TelegramUser
    """
    TelegramUser.objects.filter(user_id=user_id).update(**kwargs)

