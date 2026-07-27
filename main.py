import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

BOT_TOKEN = "8646657966:AAGGjfZq3WU0MCIq2hkTQy1fbRIjFSV7jlo"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        "Я твой студенческий помощник.\n\n"
        "Доступные команды:\n"
        "/deadlines — список горящих дедлайнов\n"
        "/add_deadline — добавить новый дедлайн\n"
        "/gpa — посчитать средний балл"
    )


async def main():
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
