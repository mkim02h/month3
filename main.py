# # import time

# # def task(name, seconds):
# #     print(f'Упала {name}, выполняю задачу!')
# #     time.sleep(seconds)
# #     print(f'{name} готово!')

# # task('Задача1', 6)
# # task('Задача2', 3)
# # task('Задача3', 1)  

# import asyncio

# async def task(name, seconds):
#     print(f'Упала {name}, выполняю задачу!')
#     await asyncio.sleep(seconds)
#     print(f'{name} готово!')

# async def main():
#     await asyncio.gather(
#         task('Задача1', 6),
#         task('Задача2', 3),
#         task('Задача3', 1)
#     )
# asyncio.run(main())

import asyncio
from aiogram import Bot, Dispatcher, F
from src.handlers import router
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
print('Бот запущен!')


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())