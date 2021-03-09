#!/usr/bin/env python
# -*- coding: utf-8 -*-

from misc import dp, bot
from aiogram import types
from .list import get_rates
import text


@dp.message_handler(commands=['exchange'])
async def exchange_command(message: types.Message):
    user_id = message["from"].id
    mssg_data = message["text"][10:].upper().split(" ")
    if len(mssg_data) == 1:
        await bot.send_message(user_id, text.EXCHANGE_USAGE)
        return
    exchange_currency = mssg_data[-1]
    amount = -1
    for item in mssg_data:
        if amount != -1:
            break
        if item.isdigit():
            amount = int(item)
        elif item[0] == '$':
            amount = int(item[1:])
        elif item[-1] == '$':
            amount = int(item[:-1])
        elif item.find("USD") != -1:
            if item != "USD":
                amount = int(item.replace("USD", ""))
    try:
        rate = get_rates()[exchange_currency]
    except:
        await bot.send_message(user_id, text.EXCHANGE_USAGE)
        return
    exchanged_amount = float(amount) * float(rate)
    exchanged_amount = "%.2f" % exchanged_amount
    await bot.send_message(user_id, f"${exchanged_amount}")
