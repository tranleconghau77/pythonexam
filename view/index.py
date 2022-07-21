import asyncio
import tornado.web
import os
import json

from controllers.main_handler import MainHandler
from controllers.random_value_player_handler import RandomValuePlayerHandler
from controllers.login import Login
from controllers.verify_login import VerifyLogin
from controllers.guess_value import GuessValue


# class GuessValue(tornado.web.RequestHandler):
#     def post(self):
#         self.write(self.request.body)
#         guess_result = self.request.body
#         self.write(result_compare)
#         if guess_result == result_compare:
#             self.write("You win")
#         else:
#             self.write("You lose")
#         # self.redirect("/")


def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), 'static')
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
    print("Server running")
    result_compare = None
    asyncio.run(main())
