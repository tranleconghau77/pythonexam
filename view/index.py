import asyncio
from email import header
import tornado.web
import os

import sys
sys.path.append("..")

from controllers.tester import test


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        testabc = test()
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("index.html", title="My title", items=items, test = testabc)

class RandomValuePlayerHandler(tornado.web.RedirectHandler):
    def get(self):
        self.response()


def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), 'static')
    }
    return tornado.web.Application([
       (r"/", MainHandler),
       (r"/randomcard", RandomValuePlayerHandler)
        ],
        **settings
    )
async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    print("Server running")
    asyncio.run(main())