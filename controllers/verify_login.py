import tornado

from functions.file_manager import FileManager
from functions.player import player
from services.connect_db import connect_db


class VerifyLogin(tornado.web.RequestHandler):
    def post(self):
        username = self.request.body

        db = connect_db()

        game_cards = db.game_cards
        result = game_cards.customers

        print('Total Record for the collection: ' + str(result.count()))
        for record in result.find().limit(10):
            print(record)

        self.write(str(result))

        # if username not in data:
        #     new_player = player(username)
        #     print(type(new_player.__dict__))
        #     data.append(new_player.__dict__)
