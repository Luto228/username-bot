from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def continue_find_username() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton(text="next", callback_data="next_button"),
                InlineKeyboardButton(text="leave", callback_data="leave_button"),
            ]
        ]
    )

    return keyboard