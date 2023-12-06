from fastapi import HTTPException
from bson.objectid import ObjectId
from server.config import events_collection

# helper
def event_helper(event) -> dict:
    return {
        "id": str(event["_id"]),
        "name": event["name"]
    }


# Retrieve all event present in the database
async def retrieve_events():
    events = []
    async for event in events_collection.find():
        events.append(event_helper(event))
    return events