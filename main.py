import logging
import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start, system, phone, email

from bot.bot import bot


dp = Dispatcher(storage=MemoryStorage())

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s|%(levelname)s|%(name)s|%(message)s",
    datefmt='%Y-%m-%d|%H:%M:%S'
)


async def main() -> None:
    dp.include_router(start.router)
    dp.include_router(system.router)
    dp.include_router(phone.router)
    dp.include_router(email.router)
    logger.warning("Starting aiogram polling")

    await asyncio.gather(dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()))


if __name__ == "__main__":
    asyncio.run(main())
