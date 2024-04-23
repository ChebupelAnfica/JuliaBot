from aiogram import F, types
from states.data_collection import Form
from aiogram.fsm.context import FSMContext
from loader import dp, bot
import keyboards
import logging


@dp.message(Form.phone)
async def process_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    try:
        await message.answer("Также нам понадобится твоя почта, чтобы добавить в список предзаписи на геткутсе.",
                             reply_markup=keyboards.default.main_menu.reset_button)
        await state.set_state(Form.email)
    except Exception as ex:
        logging.error(ex)
