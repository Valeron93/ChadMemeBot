import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import message, InputFile

import settings
import mv,img
import os

storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)

bot = Bot(token = settings.TOKEN)
dp = Dispatcher(bot, storage=storage)

class VideoForm(StatesGroup):
    string1 = State()
    string2 = State()


@dp.message_handler(state='*', commands='image')
async def image(msg: types.Message, state: FSMContext):
    await VideoForm.string1.set()
    async with state.proxy() as data:
        data['action'] = 'image'
    await msg.answer('Enter string 1')
    

@dp.message_handler(state = '*', commands='video')
async def video(msg: types.Message, state: FSMContext):
    await VideoForm.string1.set()
    async with state.proxy() as data:
        data['action'] = 'video'
    await msg.answer('Enter string 1')
    

@dp.message_handler(state=VideoForm.string1)
async def str1(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['string1'] = msg.text
    await VideoForm.next()
    await msg.answer('Enter string 2')


@dp.message_handler(state=VideoForm.string2)
async def str2(msg: types.Message, state: FSMContext):
    action = ''
    string1 = ''
    string2 = msg.text

    async with state.proxy() as data:
        string1 = data['string1']
        action = data['action']

    await msg.answer('Please wait')


    if action == 'video':
        path = mv.movie(string1, string2)
        await msg.answer_video(InputFile(path))
        os.remove(path)

    elif action == 'image':
        path = img.maker(string1, string2)
        await msg.answer_photo(InputFile(path))
        os.remove(path)

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
