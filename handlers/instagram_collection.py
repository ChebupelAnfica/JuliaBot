from aiogram import F, types
from states.data_collection import Form
from aiogram.fsm.context import FSMContext
from loader import dp, bot

import keyboards
import logging


@dp.message(Form.instagram)
async def process_instagram(message: types.Message, state: FSMContext):
    await state.update_data(instagram=message.text)
    try:
        await message.answer(
            "Пожалуйста, нажмите на кнопку ниже и предоставьте свой контактный номер.",
            reply_markup=keyboards.default.main_menu.contact
        )
        await state.set_state(Form.phone)
    except Exception as ex:
        logging.error(ex)
