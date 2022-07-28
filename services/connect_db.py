from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("./.env")

MONGO_URI = os.getenv("MONGO_URI")

def connect_db():
    try:
        myclient = MongoClient(MONGO_URI)
        print("MONGO Connect")
        return myclient
    except:
        print("Do not connect MONGO DB")
        return
