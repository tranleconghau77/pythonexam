import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")


def connect_db():
    try:
        myclient = pymongo.MongoClient(
            f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster0.cfll8.mongodb.net/?retryWrites=true&w=majority")

        print("MONGO Connect")
        return myclient
    except:
        print("Do not connect MONGO DB")
        return
