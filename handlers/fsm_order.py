from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class Order(StatesGroup):
    name = State()
    count = State()
    adress = State()

router_order = Router()

@router_order.message(Command("order"))
async def order_start_fsm(message: Message, state: FSMContext):
    await message.answer("Введите название товара:")
    await state.set_state(Order.name)

@router_order.message(Order.name)
async def order_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Укажите количество товара:')
    await state.set_state(Order.count)


@router_order.message(Order.count)
async def order_count(message: Message, state: FSMContext):
    await state.update_data(count=message.text)
    if not message.text.isdigit():
        await message.answer('Пожалуйста, введите корректное количество товара.')
        return
    count = int(message.text)
    await message.answer('Укажите адрес доставки:')
    await state.set_state(Order.adress)

@router_order.message(Order.adress)
async def order_adress(message: Message, state: FSMContext):
    await state.update_data(adress=message.text)
    data = await state.get_data()
    await message.answer(f'Ваш заказ: \nНазвание товара: {data['name']}' 
                         f'\nКоличество товара: {data['count']} \nАдрес доставки: {data['adress']}')
    await state.clear()