# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)
from ORM.orm import create_pool

__author__ = 'Administrator'


import asyncio, os, json, time
from www import app


# @asyncio.coroutine
def init(loop):
    # yield from create_pool(loop=loop, user='xiaoabiang', password='xiaoabiang', db='awesome')
    app.run(debug=True)
    # app = web.Application(loop=loop)
    # app.router.add_route('GET', '/', index)
    # srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    # logging.info('server started at http://127.0.0.1:9000...')
    # print(logging)
    # return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

