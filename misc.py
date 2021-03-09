#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from aiogram import Bot, Dispatcher
from config import BOT_API, DATABASE
from sqlite import SQLite

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_API)
dp = Dispatcher(bot=bot)
db = SQLite(database=DATABASE)
