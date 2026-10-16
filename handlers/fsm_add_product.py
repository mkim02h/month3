from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class Add_Product(StatesGroup):
    name = State()
    price = State()
    description = State()
    photo = State()

router_add_product = Router()

@router_add_product.message(Command("add_product"))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer("Введите название товара:")
    await state.set_state(Add_Product.name)

@router_add_product.message(Add_Product.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите цену товара:")
    await state.set_state(Add_Product.price)

@router_add_product.message(Add_Product.price)
async def add_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('Введите описание товара:')
    await state.set_state(Add_Product.description)

@router_add_product.message(Add_Product.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Отправьте фото товара:')
    await state.set_state(Add_Product.photo)

@router_add_product.message(Add_Product.photo)
async def add_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)

    data = await state.get_data()

    await message.answer_photo(photo=data['photo'],
    caption=f'Данные товара: \nНазвание: {data['name']}'
    f'\nЦена: {data['price']} \nОписание: {data['description']}')
    await state.clear()