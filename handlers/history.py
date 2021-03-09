#!/usr/bin/env python
# -*- coding: utf-8 -*-

from misc import dp, bot
from aiogram import types
import text
import requests
import json
from datetime import datetime
from time import time
from config import API_URL
import pandas
import matplotlib.pyplot as plt


@dp.message_handler(commands=['history'])
async def history_command(message: types.Message):
    user_id = message["from"].id
    mssg_data = message["text"].upper().split(" ")
    if len(mssg_data) == 1 or len(mssg_data) != 5:
        await bot.send_message(user_id, text.HISTORY_USAGE)
        return

    if len(mssg_data[1]) == 7:
        base_curr = mssg_data[1][0:3].upper()
        ex_curr = mssg_data[1][4:].upper()
    else:
        await bot.send_message(user_id, text.HISTORY_USAGE)
        return
    if mssg_data[-2].isdigit():
        # 86400 is a number of seconds in a day
        period = int(mssg_data[-2]) * 86400
        t = int(time())
        end_time = datetime.date(datetime.fromtimestamp(t))
        start_time = datetime.date(datetime.fromtimestamp(t - period))
        req_str = f"{API_URL}history?start_at={start_time}&end_at={end_time}&base={base_curr}&symbols={ex_curr}"
        data = json.loads(requests.get(url=req_str).content.decode("utf-8"))['rates'].items()
        arr = [{"date": item[0], "rate": float(item[1][ex_curr])} for item in sorted(data)]
        if len(arr) < 1:
            await bot.send_message(user_id, text.NO_DATA_ERROR)
            return
        dataset = pandas.DataFrame(arr)
        dataset.plot(x="date", y="rate", title='Exchange rates')
        plt.savefig("visualisation.png")
        with open("visualisation.png", "rb") as pic:
            await bot.send_photo(user_id, pic)
    else:
        await bot.send_message(user_id, text.WRONG_PERIOD_ERROR)
        return
