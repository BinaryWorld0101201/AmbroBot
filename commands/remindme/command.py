from telegram.ext import run_async

from commands.remindme.keyboards import time_options_keyboard
from utils.decorators import send_typing_action, log_time


@log_time
@send_typing_action
@run_async
def remind_me(bot, update, chat_data, args):
    if not args:
        update.message.reply_text(
            'Me tenés que dar algo que recordar! `/remind comprar frutas`',
            parse_mode='markdown',
        )
        return

    # Save what the bot should remind the user
    chat_data['to_remind'] = ' '.join(args)
    chat_data['user'] = _tag_user(update.message.from_user)

    # Offer when the user wants to be reminded (5 minutes, 2 hours)
    time_options = time_options_keyboard()
    update.message.reply_text(
        text='Elegí cuando querés que te recuerde el evento', reply_markup=time_options
    )


def _tag_user(user):
    if user.username:
        return f'@{user.username}'
    else:
        return f"[@{user.first_name}](tg://user?id={user.id})"
