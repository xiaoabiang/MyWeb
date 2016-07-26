# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)

__author__ = 'Administrator'


import asyncio
from www import app


def init(loop):
    app.run(debug=True)

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

