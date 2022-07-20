import asyncio
from email import header
import tornado.web
import os

from controllers.compare_value import compare_value
from controllers.card_player import card_player
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("view/index.html", title="My title", items=items)

class RandomValuePlayerHandler(tornado.web.RequestHandler):
    def get(self):
        data = card_player()
        global result_compare
        result_compare = compare_value(data["card_one"], data["card_two"])
        self.render("view/home.html",data = data)

class GuessValue(tornado.web.RequestHandler):
    def post(self):
        self.write(self.request.body)
        guess_result = self.request.body
        self.write(result_compare)
        if guess_result == result_compare:
            self.write("You win")
        else:
            self.write("You lose")
        # self.redirect("/")

def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), 'static')
    }
    return tornado.web.Application([
       (r"/", MainHandler),
       (r"/randomcard", RandomValuePlayerHandler),
       (r"/guess_value",GuessValue)
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