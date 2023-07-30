from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Contacts'),
                KeyboardButton(text='Balance')
            ],
            [
                KeyboardButton(text='Account')
            ],
            [
                KeyboardButton(text='Check')
            ]
        ],
        resize_keyboard=True
    )

agree_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Agree')
            ]
        ],
        resize_keyboard=True
    )

search_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Search by FIO')
            ],
            [
                KeyboardButton(text='Search by telephone'),
                KeyboardButton(text='Search by email')
            ]
        ],
        resize_keyboard=True
    )

cancel_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Cancel')
            ]
        ],
        resize_keyboard=True
    )
