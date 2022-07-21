import tornado


from functions.compare_value import compare_value


class GuessValue(tornado.web.RequestHandler):
    def post(self):
        self.write(self.request.body)
        data = self.request.body
        self.write(data)
        # guess_result = self.request.body
        # self.write(result_compare)
        # if guess_result == result_compare:
        #     self.write("You win")
        # else:
        #     self.write("You lose")
        # self.redirect("/")
