from apps.telegram import steps, db_connection
import json


def start_message_view(message, bot):
    user = db_connection.get_user_from_db(message)
    text = f'Assalomu Alaykum {message.from_user.first_name}' \
           f'\n\nEco Botga Xush kelibsiz'
    text2 = '''
            🔸 @BlogHelper_bot v2020.10 - Bot returns json for all sent messages.

Messages editing and inline queries are also supported.

For support or if you have questions about bots' development - contact @BlogHelper_bot

Enjoy! ☺️
    '''
    bot.send_message(message.from_user.id, text2)


def send_message_view(message, bot):
    user = db_connection.get_user_from_db(message)
    data = f'''
            'message': ''' + '{' + f'''
                'message_id': {message.message_id},
                'from':''' + '{' + f'''
                    'id': {message.from_user.id},
                    'is_bot': {message.from_user.is_bot},
                    'first_name': {message.from_user.first_name},
                    'language_code': {message.from_user.language_code}
                ''' + '}' + f''',
                'chat': ''' + '{' + f'''
                    'id': {message.chat.id},
                    'first_name': {message.chat.first_name},
                    'tyep': {message.chat.type}
                ''' + '}' + f''',
                'date': {message.date},
                'text': {message.text}
            ''' + '}' + f'''
        '''
    data2 = {
        'message': {
            'message_id': message.message_id,
            'from': {
                'id': message.from_user.id,
                'is_bot': message.from_user.is_bot,
                'first_name': message.from_user.first_name,
                'language_code': message.from_user.language_code
            },
            'chat': {
                'id': message.chat.id,
                'first_name': message.chat.first_name,
                'type': message.chat.type,
            },
            'date': message.date,
            'text': message.text
        }
    }
    bot.send_message(message.from_user.id, json.dumps(data2))
