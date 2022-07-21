import tornado
import json

from functions.file_manager import FileManager
from functions.player import player


def getData():

    # loading a file
    with FileManager('data.json', 'r') as f:
        data = json.load(f)
    return data


class VerifyLogin(tornado.web.RequestHandler):
    def post(self):
        username = self.request.body
        print(type(username))
        data = getData()

        if username not in data["data"]:
            new_player = player(username)
            print(type(new_player.__dict__))
            print("type of", type(data))
            print("type of", type(data["data"]))
            data["data"].append(new_player.__dict__)
            with FileManager("data.json", "w") as f:
                f.dump(str(data))
        print(data)
        # self.write(data)
        self.write(username)
