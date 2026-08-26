from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def category_inline_keyboard() -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup( 
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Default", callback_data="default_categories"),
                    InlineKeyboardButton(text="Custom", callback_data="custom_categories")
                ]
            ]
        )
        return keyboard