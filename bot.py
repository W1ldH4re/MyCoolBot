# Асинхронный цикл для работы бота
import asyncio

# импортируем класс бота из библиотеки aiogram
from aiogram import Bot, Dispatcher

# импортируем токен бота из файла config.py
from config import TOKEN

# Роутеры
from handlers.start import router as start_router
from handlers.create_room import router as create_router
from handlers.join_room import router as join_router

# Создаём экземпляр бота
bot = Bot(token=TOKEN)

# Создаём диспетчер для обработки сообщений
dp = Dispatcher()

# Регистрируем роутеры
dp.include_router(start_router)
dp.include_router(create_router)
dp.include_router(join_router)

# Функция для запуска бота
async def main():
    try:
        print("Бот запущен...")
        await dp.start_polling(bot)

    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
        await asyncio.sleep(5)  # Подождать 5 секунд перед повторной попыткой

# Запускаем бота
if __name__ == "__main__":
    asyncio.run(main())