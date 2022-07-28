import tornado
import pymongo

from functions.player import player
from services.connect_db import connect_db

class VerifyLogin(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "text/plain")
        username = self.request.body

        print(username)
        print(username.decode("utf-8"))
        print(type(username))

        cluster = connect_db()


        db = cluster["game_cards"]
        collection = db["customers"]


        list_data = list(collection.find({}))

        x = [x for x in list_data if username.decode("utf-8") == x ]

        # for result in results:
        #     print(result["_id"])

        print("find", x)
        self.write("Hello")
