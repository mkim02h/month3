from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from src.keyboards import reply_keyboard, inline_keyboard, quiz_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}! Я твой бот, который умеет выполнять задачи асинхронно.',
        reply_markup=reply_keyboard 
    )
    print(f'Пользователь {message.from_user.full_name} с никнеймом {message.from_user.username} зашел в бота.')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f'/start - начать работу с ботом\n'
        '/help - получить справку по командам',
        reply_markup=inline_keyboard
    
    )

@router.message(F.text.lower() == 'группа')
async def get_group(message: Message):
    await message.answer('Твоя группа 70-2!')

@router.message(F.text == 'Контакты')
async def get_contacts(message: Message):
    await message.answer('Магазин "WhyMusic"\nАдрес: г. Бишкек, Московская, 121\nТелефон: +996555176671')

@router.message(F.text == 'Каталог')
async def get_catalog(message: Message):
    await message.answer('Гитара - 46000 сом\nБарабаны - 97000 сом\nСаксофон - 67000 сом\nФлейта - 23000 сом\nПианино - 150000 сом')


@router.callback_query(F.data == 'start_game')
async def start_game(callback: CallbackQuery):
    await callback.answer('Начинаем игру!', show_alert=True)
    await callback.message.answer('Первый вопрос: Сколько будет 2 + 2?',
    reply_markup = quiz_keyboard
    )
    
@router.callback_query(F.data == 'ans4_correct')
async def correct_answer(callback: CallbackQuery):
    await callback.answer('Правильный ответ!', show_alert=True)
    await callback.message.answer('Поздравляю! Вы ответили правильно!')

@router.callback_query(F.data == 'ans3')
async def wrong_answer_3(callback: CallbackQuery):
    await callback.answer('Ошибка!', show_alert=True)
    await callback.message.answer('Неверно, 4.')

@router.callback_query(F.data == 'ans6')
async def wrong_answer_6(callback: CallbackQuery):
    await callback.answer('Ошибка!', show_alert=True)
    await callback.message.answer('Неверно, 4.')

@router.callback_query(F.data == 'about_me')
async def about_me(callback: CallbackQuery):
    await callback.answer('Информация обо мне', show_alert=True)
    await callback.message.answer('Студент группы 70-2, обучаюсь на 3 месяце курса Backend-разработчик на Python в IT-академии Geeks.')

@router.message()
async def echo(message: Message):
    await message.answer(f'Вы написали: {message.text}')
