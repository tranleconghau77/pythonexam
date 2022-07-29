import tornado
import json
import pymongo
import motor.motor_asyncio
import asyncio
# from pymongo import MongoClient
from bson import json_util, ObjectId

from functions.player import player
from services.connect_db import connect_db

class VerifyLogin(tornado.web.RequestHandler):
    async def post(self):
        
        username = self.get_argument("username")

        cluster = await connect_db()

        db =  cluster.game_cards
        collection =  db.customers


        # list_data = jsonify(((collection.find({}))))
        print(await collection.find_one({"_id":1}))
    
        # list_data = list(collection.find({}))

        # result = json.dumps(list_data,default=json_util.default)

        # x = [x for x in list_data if username.decode("utf-8") == x ]

        # for result in list_data:
        #     print(result["_id"])

        # print("find", x)
        self.write({
            "data" : "abc"
        })
