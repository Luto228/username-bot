from email import message
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from Inline_keyboard import category_inline_keyboard 

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer("Hello! I will help you find a really good username!")
@dp.message(Command("username"))
async def command_username(message: Message):
    await message.answer("Do you want default categories or custom categories?")
    await message.answer("Default categories: \n 8(minimal length), \n Both(noun and verb), \n yes(use AI), \n 2(minimal rarity)")
    await message.answer("Choose an option:", reply_markup=await category_inline_keyboard())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())