from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

contacts_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='TG', url='http://132.com'),
                InlineKeyboardButton(text='Vk', url='http://123.com')
            ]
        ]
    )


def set_balance_keyboard(user_id) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Share link', url=f'https://t.me/share/url?url=https://t.me/https://t.me/edfghbjnklp_bot?start=BRANDkrg{user_id}'),
            ]
        ]
    )
