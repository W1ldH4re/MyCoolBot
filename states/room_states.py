from aiogram.fsm.state import (
    State,
    StatesGroup
)

class JoinRoomState(
    StatesGroup
):
    waiting_room_code = State()