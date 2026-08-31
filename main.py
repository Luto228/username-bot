from email import message
import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv
from Inline_keyboard import category_inline_keyboard 
from start_find_username import start_find_username

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer("Hello! I will help you find a really good username! \n To start the process, please enter the command /username")
@dp.message(Command("username"))
async def command_username(message: Message):
    await message.answer("Do you want default categories or custom categories?")
    await message.answer("Default categories: \n 8(minimal length), \n yes(nouns), yes(verbs), yes(adjectives) or just y, y, y, \n yes(use AI), \n 2(minimal rarity)")
    await message.answer("Choose an option:", reply_markup=await category_inline_keyboard())

@dp.callback_query(F.data == "default_categories")
async def def_categories(callback: CallbackQuery):
    await callback.answer("default")
    await callback.message.edit_text("Great! wait until i generate username from default categories.")
    found_username = start_find_username(8, "y", "y", "y", "y", 2)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())