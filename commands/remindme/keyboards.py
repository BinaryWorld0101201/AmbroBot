from telegram import InlineKeyboardMarkup, InlineKeyboardButton as Button

from commands.remindme.constants import MINUTE, HOUR, DONE, REMIND_AGAIN
from commands.remindme.utils import remind_time


def time_options_keyboard():
    buttons = [
        [
            Button('5 Mins', callback_data=remind_time(5 * MINUTE)),
            Button('10 Mins', callback_data=remind_time(10 * MINUTE)),
            Button('20 Mins', callback_data=remind_time(20 * MINUTE)),
            Button('30 Mins', callback_data=remind_time(30 * MINUTE)),
        ],
        [
            Button('1 Hour', callback_data=remind_time(HOUR)),
            Button('2 Hours', callback_data=remind_time(2 * HOUR)),
            Button('4 Hours', callback_data=remind_time(4 * HOUR)),
            Button('8 Hours', callback_data=remind_time(8 * HOUR)),
        ],
        [
            Button('12 hours', callback_data=remind_time(12 * HOUR)),
            Button('24 hours', callback_data=remind_time(24 * HOUR)),
            Button('48 hours', callback_data=remind_time(48 * HOUR)),
        ],
    ]

    return InlineKeyboardMarkup(buttons)


def remind_again_or_done():
    buttons = [
        [
            Button('✅ Listo', callback_data=DONE),
            Button('Recordar de nuevo ⏱', callback_data=REMIND_AGAIN),
        ]
    ]
    return InlineKeyboardMarkup(buttons)
