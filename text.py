#!/usr/bin/env python
# -*- coding: utf-8 -*-


START_MESSAGE = "Hi. I am a currency bot.\n\n" \
                "/list or /lst - returns list of all available rates\n" \
                "/exchange - converts the currencies\n" \
                "converts - shows the history of the currency's rate for the selected period"
LIST_MESSAGE = "Here's the latest currency rates: \n\n"
ERROR_MESSAGE = "Ooops... Something went wrong."
WRONG_PERIOD_ERROR = "You have misspelled the period of time. Isn't it?"
NO_DATA_ERROR = "Unfortunately, there is no any data for the selected currencies."
HISTORY_USAGE = "How to use the command:\n\n" \
                "/history <base_currency>/<second_currency> for <number> day(s)"
EXCHANGE_USAGE = "How to use the command:\n\n" \
                "/exchange <amount> <first_currency> to <second_currency>"
