from aiogram.types import (ReplyKeyboardMarkup, 
                            KeyboardButton,
                            InlineKeyboardMarkup,
                            InlineKeyboardButton)

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')],
])

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перейти на сайт', url='https://geeks.kg')],
    [InlineKeyboardButton(text='Начать игру', callback_data='start_game')],
    [InlineKeyboardButton(text='Мой Инстаграм', url='https://instagram.com/mkim02?vrfl=MTA0ZGdwb3YzY2YzNQ%3D%3D&utm_source=qr')],
    [InlineKeyboardButton(text='Обо мне', callback_data='about_me')],
    [InlineKeyboardButton(text='Мой GitHub', url='https://github.com/mkim02h')]
])

quiz_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='3', callback_data='ans3')],
    [InlineKeyboardButton(text='6', callback_data='ans6')],
    [InlineKeyboardButton(text='4', callback_data='ans4_correct')],
])