from aiogram import Bot, Dispatcher
from database.models import models_main
from config import TOKEN
from database.models import models_main
import asyncio



async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher
    dp.include_router(dp)
    await dp.start_polling(bot) #Держит бота в активном положении
    await models_main()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
