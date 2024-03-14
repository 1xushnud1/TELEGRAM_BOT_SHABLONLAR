import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from root_shablon import TOKEN

dp = Dispatcher()


@dp.message(CommandStart()) # Bu funksiya uchun shablon.Shu funksiyamizga qarab qolgan funksiyalarni tuzib chiqasiz.
async def start(message: Message):
    await message.answer("Hello User!")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())