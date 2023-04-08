import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import config
from router import test, en_lng, rus_ln, nav, tualet, exits, meeting, event




async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.BOT_API_TOKEN)

    #-----------------------------------
    dp.include_router(test.router)
    #-----------------------------------
    dp.include_router(rus_ln.router)
    #-----------------------------------
    dp.include_router(en_lng.router)
    # -----------------------------------
    dp.include_router(nav.router)
    # -----------------------------------
    dp.include_router(tualet.router)
    # -----------------------------------
    dp.include_router(exits.router)
    # -----------------------------------
    dp.include_router(meeting.router)
    # -----------------------------------
    dp.include_router(event.router)
    # -----------------------------------




    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())