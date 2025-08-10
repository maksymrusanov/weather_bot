from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from tg_bot.states import weather
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

router = Router()


@router.message(CommandStart())
async def start(message: Message, state):
    await state.set_state(weather.location)
    await message.answer(text='Enter your location please: ', reply_markup=ReplyKeyboardRemove())


@router.message(weather.location)
async def process_location(message, state):
    await state.update_data(location=message.text)
    await state.set_state(weather.days)


@router.message(weather.days)
async def process_days(message, state):
    await message.answer(text='Enter you days: ', reply_markup=ReplyKeyboardRemove())
    await state.update_data(days=message.text)
    get = await state.get_data()
    await
