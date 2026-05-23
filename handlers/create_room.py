from aiogram import Router
from aiogram.types import Message

from rooms import rooms, generate_room_code

router = Router()

@router.message(lambda m: m.text == "🆕 Создать комнату")
async def create_room(message: Message):
    # Генерируем уникальный код комнаты
    code = generate_room_code()

    # Создаём новую комнату и сохраняем её в словаре rooms
    rooms[code] = {
        "owner": message.from_user.id,  # ID пользователя, который создал комнату
        "quest": None,  # Вопрос для раунда (пока None)
        "turn": message.from_user.id,  # Номер текущего раунда
        "category": None,  # Категория для раунда (пока None)
        "players": [message.from_user.id]  # Список игроков в комнате (пока только создатель)
    }

    # Отправляем пользователю сообщение с кодом комнаты
    await message.answer(
        f"Комната создана!\n\n" 
        f"Код комнаты: {code}\n\n"
        f"Поделитесь этим кодом с друзьями, чтобы они могли присоединиться к вашей комнате."
    )