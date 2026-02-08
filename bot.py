import logging
from aiogram import Bot, Dispatcher, executor, types
import os

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Salom!\n\n"
        "Bu PayReminder bot.\n"
        "Kommunal to‘lovlarni unutmaslikka yordam beraman.\n\n"
        "🧾 /add — yangi to‘lov qo‘shish\n"
        "📅 /list — to‘lovlar ro‘yxati"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
