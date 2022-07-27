from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_CONNECT")


def connect_db():
    try:
        print("aaaa")
        myclient = MongoClient(MONGO_URI)
        print("MONGO Connect")
        return myclient
    except:
        print("Do not connect MONGO DB")
        return
