import tornado
from functions.card_player import card_player
from functions.compare_value import compare_value


class RandomValuePlayerHandler(tornado.web.RequestHandler):
    def get(self):
        data = card_player()
        # result_compare = compare_value(data["card_one"], data["card_two"])
        self.render("../view/home.html", data=data)
