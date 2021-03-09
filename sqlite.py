#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


class SQLite:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_latest_request(self):
        with self.connection:
            data = self.connection.execute("SELECT * FROM 'exchange_rates' ORDER BY id DESC LIMIT 1").fetchone()
            return data

    def update_rates(self, timestamp: int, data: str):
        with self.connection:
            self.connection.execute("INSERT INTO 'exchange_rates' ('request_time', 'data')"
                                    "VALUES(?, ?)", (timestamp, data, ))