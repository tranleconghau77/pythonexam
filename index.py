import asyncio
import tornado.web
import os

from controllers.main_handler import MainHandler
from controllers.random_value_player_handler import RandomValuePlayerHandler
from controllers.login import Login
from controllers.verify_login import VerifyLogin
from controllers.guess_value import GuessValue
from services.connect_db import connect_db


def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), 'view/static')
    }
    return tornado.web.Application(
        handlers=[
            (r"/", MainHandler),
            (r"/login", Login),
            (r"/verifyLogin", VerifyLogin),
            (r"/randomcard", RandomValuePlayerHandler),
            (r"/guess_value", GuessValue)
        ],
        **settings
    )


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    print("Server running port 8888")
    result_compare = None
    asyncio.run(main())
    connect_db.close()
