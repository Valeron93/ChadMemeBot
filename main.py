import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import message, InputFile

import settings
import mv
import os


storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)

bot = Bot(token = settings.TOKEN)
dp = Dispatcher(bot, storage=storage)

class VideoForm(StatesGroup):

    string1 = State()
    string2 = State()

'''class ImageForm(StatesGroup):

    string1 = State()
    string2 = State()
'''
@dp.message_handler(state='*', commands='image')
async def image(msg: types.Message, state: FSMContext):
    await VideoForm.string1.set()
    async with state.proxy() as data:
        data['typ'] = 'image'
    await msg.answer('Enter string 1')
    

@dp.message_handler(state = '*', commands='video')
async def video(msg: types.Message, state: FSMContext):
    await VideoForm.string1.set()
    async with state.proxy() as data:
        data['typ'] = 'video'
    await msg.answer('Enter string 1')
    

@dp.message_handler(state=VideoForm.string1)
async def str1(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['string1'] = msg.text
    await VideoForm.next()
    await msg.answer('Enter string 2')


@dp.message_handler(state=VideoForm.string2)
async def str2(msg: types.Message, state: FSMContext):
    typ = ''
    string1 = ''
    string2 = msg.text
    async with state.proxy() as data:
        string1 = data['string1']
        typ = data['typ']
    await msg.answer('Please wait')

    if typ == 'video':
        path = mv.movie(string1, string2)
        file = InputFile(path)
        await msg.answer_video(file)
        os.remove(path)
    elif typ == 'image':
        pass

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    