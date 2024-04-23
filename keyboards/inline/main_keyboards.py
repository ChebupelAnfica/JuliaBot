from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

wardrobe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Составить капсульный гардероб", callback_data="btn_request_capsule")
        ],
        [
            InlineKeyboardButton(text="Научиться сочетать цвета", callback_data="btn_request_color")
        ],
        [
            InlineKeyboardButton(text="Одеться по своему типажу", callback_data="btn_request_dress")
        ],
        [
            InlineKeyboardButton(text="Найти свой стиль", callback_data="btn_request_style")
        ]
    ],
)
