#!/usr/bin/env python
# -*- coding: utf-8 -*-

from misc import dp, bot, db
from aiogram import types
from config import API_URL
import text
import requests
import json
from time import time

REQUEST_TYPE = "latest?base="
BASE_CURRENCY = "USD"
UPDATING_TIME = 600


def get_rates():
    time_stamp = int(time())
    latest_request_time = 0 if db.get_latest_request() is None else db.get_latest_request()[0]
    if time_stamp - latest_request_time > UPDATING_TIME:
        raw_data = requests.get(f"{API_URL}{REQUEST_TYPE}{BASE_CURRENCY}").content.decode('utf-8')
        if not raw_data:
            return None
        db.update_rates(timestamp=time_stamp, data=raw_data)
    else:
        raw_data = db.get_latest_request()[1]
    return json.loads(raw_data)["rates"]


@dp.message_handler(commands=['list', 'lst'])
async def list_command(message: types.Message):
    user_id = message["from"].id
    reply = text.LIST_MESSAGE
    rates = get_rates().items()
    if rates:
        for item in rates:
            currency = item[0]
            value = "%.2f" % item[1]
            reply += f"{currency}:  {value}\n"
    await bot.send_message(user_id, reply)

