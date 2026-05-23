from aiogram import Router
from aiogram.types import Message
from keyboards.menu import menu_keyboard
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Я бот для игры в Пошлые смайлы 18+. \n\n" 
        "Создай комнату или присоединись к существующей.",
        
        reply_markup=menu_keyboard
    )