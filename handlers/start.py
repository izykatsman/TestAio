from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from States.states import Start
from keyboards.Reply import agree_keyboard, main_keyboard
from messages import hellow_message

router = Router()


@router.message(Command('start'))
async def triggers_handler(message: Message, state: FSMContext) -> None:
    # TODO проверить есть ли пользователь, если нет, перевести сразу в главное меню
    await message.answer(hellow_message)
    # await message.answer_document()
    await message.answer("Are you agree?", reply_markup=agree_keyboard)
    await state.set_state(Start.get_start_agree)


@router.message(Text('Agree', ignore_case=True), Start.get_start_agree)
async def get_numbers(message: Message, state: FSMContext) -> None:
    # TODO вывести данные о пользователе
    await message.answer(f"""Регистрация успешно завершена
У вас есть {0} бесплатных запросов
Главное меню""", reply_markup=main_keyboard)
    await state.clear()
