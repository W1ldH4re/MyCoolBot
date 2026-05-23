from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter   # <-- ВАЖНО

from rooms import rooms
from states.room_states import JoinRoomState

router = Router()


# Вход в режим ожидания кода
@router.message(F.text == "🔑 Войти в комнату")
async def ask_room_code(message: Message, state: FSMContext):

    await state.set_state(JoinRoomState.waiting_room_code)

    await message.answer("🔑 Введи код комнаты:")


# ВВОД КОДА (ИСПРАВЛЕНО)
@router.message(StateFilter(JoinRoomState.waiting_room_code))
async def join_room(message: Message, state: FSMContext):

    code = message.text.strip()

    if code not in rooms:

        await message.answer("❌ Комната не найдена.")
        return

    room = rooms[code]

    if room["guest"] is not None:

        await message.answer("❌ Комната уже занята.")
        return

    room["guest"] = message.from_user.id
    room["players"].append(message.from_user.id)

    await state.clear()

    await message.answer("✅ Ты подключился!")

    await message.bot.send_message(
        room["owner"],
        "🎮 Второй игрок подключился!"
    )