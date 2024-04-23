import logging

from aiogram import types, F
from aiogram.fsm.context import FSMContext
from states.data_collection import Form
from loader import dp, bot


@dp.callback_query(F.data == "cancel")
async def cancel(call: types.CallbackQuery, state: FSMContext):
    try:
        await bot.delete_message(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.message(F.text == 'Сбросить анкету')
async def reset_button_handler(message: types.Message, state: FSMContext):
    try:
        await state.clear()
    except Exception as ex:
        logging.error(ex)
    try:
        await message.answer(' Давай познакомимся: Как тебя зовут?')
    except Exception as ex:
        logging.error(ex)

    try:
        await state.set_state(Form.fullname)
    except Exception as ex:
        logging.error(ex)
