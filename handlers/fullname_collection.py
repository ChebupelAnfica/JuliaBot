from aiogram import F, types
from states.data_collection import Form
from aiogram.fsm.context import FSMContext
from loader import dp, bot

import keyboards
import logging

@dp.message(Form.fullname)
async def process_fullname(message: types.Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    try:
        await message.answer("Какой запрос ты хочешь решить с помощью курса?",
                             reply_markup=keyboards.inline.main_keyboards.wardrobe_keyboard)
        await state.set_state(Form.request)
    except Exception as ex:
        logging.error(ex)


