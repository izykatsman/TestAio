from aiogram.filters.state import State, StatesGroup


class Start(StatesGroup):
    get_start_agree = State()


class Phone(StatesGroup):
    get_phone = State()
