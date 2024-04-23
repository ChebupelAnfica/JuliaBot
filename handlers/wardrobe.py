from aiogram import F, types
from states.data_collection import Form

from aiogram.fsm.context import FSMContext

from loader import dp, bot
import logging
import keyboards

@dp.callback_query(lambda query: query.data.startswith('btn_request_'))
async def button_request(callback_query: types.CallbackQuery, state: FSMContext):
    request_type = callback_query.data.split('_')[2]

    if request_type == "capsule":
        response_text = 'Составить капсульный гардероб'
    elif request_type == "color":
        response_text = 'Научиться сочетать цвета'
    elif request_type == "dress":
        response_text = 'Одеться по своему типажу'
    elif request_type == "style":
        response_text = 'Найти свой стиль'
    else:
        response_text = 'Неизвестный запрос'

    await state.update_data(request=response_text)

    try:
        await bot.answer_callback_query(callback_query.id)
    except Exception as ex:
        logging.error(ex)
    try:
        await bot.send_message(callback_query.from_user.id, 'Напиши свой Instagram',
                               reply_markup=keyboards.default.main_menu.reset_button)
    except Exception as ex:
        logging.error(ex)
    await state.set_state(Form.instagram)
