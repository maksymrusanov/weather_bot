from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from tg_bot.states import weather
from weather_app import get_weather
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
    await message.answer(text=f'you entered {message.text}')
    await message.answer(text='Enter you days:(no more then 3,sorry,i have free api ) ', reply_markup=ReplyKeyboardRemove())
    await state.set_state(weather.days)


@router.message(weather.days)
async def process_days(message, state):
    await state.update_data(days=message.text)
    get = await state.get_data()
    max_temp_c_list, cond_list, feels_like, cond_pic_list, min_temp_c_list, date_list = get_weather(
        location=get['location'], days=int(get['days']))
    await message.answer(f'Now feels like: {feels_like} °C ')
    for max_temp, cond_text, cond_pic, min_temp, date in zip(max_temp_c_list, cond_list, cond_pic_list, min_temp_c_list, date_list):
        await message.answer_photo(caption=f'city:{get['location']}\nDate:{date}\nMin temperature for today: {min_temp} °C \nMax temperature for today :{max_temp} °C \nCondition:{cond_text}\n', photo=f'https:{cond_pic}')
