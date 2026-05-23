from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🆕 Создать комнату"
            )
        ],
        [
            KeyboardButton(
                text="🔑 Войти в комнату"
            )
        ]
    ],
    resize_keyboard=True
)