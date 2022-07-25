import tornado

from functions.file_manager import FileManager
from functions.player import player


class VerifyLogin(tornado.web.RequestHandler):
    def post(self):
        username = self.request.body

        

        if username not in data:
            new_player = player(username)
            print(type(new_player.__dict__))
            data.append(new_player.__dict__)
