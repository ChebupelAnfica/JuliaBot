from aiogram import F, types
from states.data_collection import Form
from aiogram.fsm.context import FSMContext
from loader import dp, bot
from database import SessionLocal
from models import People
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select


@dp.message(Form.email)
async def process_email(message: types.Message, state: FSMContext):
    try:
        await state.update_data(email=message.text)
        user_data = await state.get_data()

        async with SessionLocal() as session:
            result = await session.execute(
                select(People).where(People.telegram_user_id == message.from_user.id))
            existing_user = result.scalars().first()

            if existing_user:
                existing_user.full_name = user_data['fullname']
                existing_user.instagram = user_data['instagram']
                existing_user.phone_number = user_data['phone']
                existing_user.email = user_data['email']
                existing_user.request = user_data['request']
            else:
                new_user = People(telegram_user_id=message.from_user.id,
                                  full_name=user_data['fullname'],
                                  instagram=user_data['instagram'],
                                  phone_number=user_data['phone'],
                                  request=user_data['request'],
                                  email=user_data['email'])
                session.add(new_user)

            await session.commit()
            await session.flush()

        await message.answer(
            text=f"Вас зовут: {user_data['fullname']}.\n"
                 f"Ваш выбранный запрос: {user_data['request']}. \n"
                 f"Ваш ник в Instagram: {user_data['instagram']}.\n"
                 f"Ваш номер телефона: {user_data['phone']}.\n"
                 f"Ваша почта: {user_data['email']}.\n"
                 f"Обязательно проверьте, нет ли опечаток и благодарим за ответы!\n"
                 f"Держи ссылку на канал https://t.me/+d2PaVPfei5MyNjg0, там будет вся важная информация о курсе и закрытые материалы от Юли"
        )
        await state.clear()
    except SQLAlchemyError as e:
        await bot.send_message(chat_id=694834819, text=f"Произошла ошибка при работе с базой данных: {e}")
    except Exception as e:
        await bot.send_message(chat_id=694834819, text=f"Произошла неизвестная ошибка: {e}")
