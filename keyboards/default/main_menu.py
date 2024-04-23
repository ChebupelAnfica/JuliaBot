from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Заполнить анкету")
        ]
    ],
    resize_keyboard=True,
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить свой контакт", request_contact=True)
        ],
        [
            KeyboardButton(text="Сбросить анкету", )
        ]
    ],
    resize_keyboard=True
)

reset_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сбросить анкету", )
        ]
    ],
    resize_keyboard=True
)
