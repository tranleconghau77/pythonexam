import tornado


class Login(tornado.web.RequestHandler):
    def get(self):

        # # Opening JSON file
        # f = await open('data.json')

        # # returns JSON object as
        # # a dictionary
        # data = await json.load(f)

        # # Iterating through the json
        # # list
        # for i in data['emp_details']:
        #     print(i)

        # # Closing file
        # await f.close()

        self.render("../view/login.html")
