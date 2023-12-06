import motor.motor_asyncio
from pymongo.collection import Collection

MONGO_DETAILS = "mongodb://root:example@mongodb:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.soczew

events_collection: Collection = database.get_collection("events")
