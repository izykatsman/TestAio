from aiogram import Router
from aiogram.filters import Text, invert_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from States.states import Phone

from keyboards.Reply import cancel_keyboard, search_keyboard

router = Router()


@router.message(Text("Search by telephone", ignore_case=True))
async def search_by_phone(message: Message, state: FSMContext) -> None:
    await message.answer("Type phone number", reply_markup=cancel_keyboard)
    await state.set_state(Phone.get_phone)


@router.message(Phone.get_phone, Text('Cancel', ignore_case=True))
async def cancel_get_phone(message: Message, state: FSMContext) -> None:
    await message.answer("Task Canceled. Chose search type", reply_markup=search_keyboard)
    await state.clear()


@router.message(Phone.get_phone)
async def search_phone(message: Message, state: FSMContext) -> None:
    # TODO сделать форматирование для номеров индии и пакистана
    await message.answer("Result")
    await state.clear()
