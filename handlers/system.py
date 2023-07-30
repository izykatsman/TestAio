from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

from keyboards.Inline import contacts_keyboard, set_balance_keyboard
from keyboards.Reply import search_keyboard

router = Router()


@router.message(Text("Contacts", ignore_case=True))
async def triggers_handler(message: Message) -> None:
    await message.answer("Our contacts", reply_markup=contacts_keyboard)


@router.message(Text("Balance", ignore_case=True))
async def triggers_handler(message: Message) -> None:
    # TODO взять из базы все данные
    await message.answer("Your balance", reply_markup=contacts_keyboard)


@router.message(Text("Account", ignore_case=True))
async def triggers_handler(message: Message) -> None:
    # TODO взять из базы все данные
    await message.answer(f"""Ваша реферальная программа

Ссылка: https://t.me/SBCheck_bot?start={message.from_user.id}
Всего приглашено человек: {0}
Всего приглашенные пополнили: {0} ₽
Доступно для вывода: {0} ₽
Уже выведено: {0} ₽""", reply_markup=set_balance_keyboard(message.from_user.id))


@router.message(Text("Check", ignore_case=True))
async def triggers_handler(message: Message) -> None:
    await message.answer(f"""Chose search type""", reply_markup=search_keyboard)
