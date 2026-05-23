import random

#Все активные комнаты хранятся в словаре, где ключ - это код комнаты, а значение - словарь с данными комнаты
rooms = {}

def generate_room_code():
    """
    Генерируем уникальный код комнаты.
    Например: 5821 
    """

    while True:
        code = str(
            random.randint(
                1000, 
                9999
            )
        )

        if code not in rooms:
            return code