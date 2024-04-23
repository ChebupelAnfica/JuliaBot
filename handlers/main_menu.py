from aiogram import F, types
from states.data_collection import Form
from aiogram.fsm.context import FSMContext
from loader import dp, bot
from aiogram.filters import StateFilter, Command

import keyboards
import logging


@dp.message(StateFilter(None), F.text == 'Заполнить анкету')
async def collect_start(message: types.Message, state: FSMContext):
    try:
        await state.clear()
    except:
        pass
    try:
        await message.answer(' Давай познакомимся: Как тебя зовут?')
    except Exception as ex:
        logging.error(ex)

    try:
        await state.set_state(Form.fullname)
    except Exception as ex:
        logging.error(ex)


