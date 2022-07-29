import pymongo
from pymongo import MongoClient
from motor import MotorClient
import asyncio
import motor.motor_asyncio
import tornado
import motor.motor_tornado
import os
from dotenv import load_dotenv

load_dotenv("./.env")

MONGO_URI = os.getenv("MONGO_CONNECT")

async def connect_db():
    try:
        MONGO_URI = os.getenv("MONGO_CONNECT")
        print(MONGO_URI)
        myclient = motor.motor_tornado.MotorClient(MONGO_URI)
        print("MONGO Connect")
        return myclient
    except:
        print("Do not connect MONGO DB")
        return

# print(asyncio.run(connect_db()))
