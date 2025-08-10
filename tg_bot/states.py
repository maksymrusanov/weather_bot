from aiogram.fsm.state import State, StatesGroup


class Weather(StatesGroup):
    location = State()
    days = State()


weather = Weather()
