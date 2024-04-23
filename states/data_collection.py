from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    fullname = State()
    request = State()
    instagram = State()
    email = State()
    phone = State()

