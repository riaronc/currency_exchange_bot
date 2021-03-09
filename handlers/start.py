#!/usr/bin/env python
# -*- coding: utf-8 -*-

from misc import dp, bot
from aiogram import types
import text


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message["from"].id
    await bot.send_message(user_id, text.START_MESSAGE)