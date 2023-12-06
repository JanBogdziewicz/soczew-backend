from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, FileResponse

from server.database.event import (
    retrieve_events
)

from server.models.event import (
    ResponseModel,
    EventSchema
)

EventRouter = APIRouter()


# Get all songs
@EventRouter.get("/", response_description="All events retrieved")
async def get_events():
    events = await retrieve_events()
    if events:
        return ResponseModel(events, "All songs retrieved successfully")
    return ResponseModel(events, "Empty list returned")
