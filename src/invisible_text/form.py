from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    get_unique_text = State()
    text_accepted = State()
