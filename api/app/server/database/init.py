from pymongo.collection import Collection
from server.config import (
    events_collection
)
import pymongo
import logging

logger = logging.getLogger(__name__)


async def create_unique_constraint(collection: Collection, fields: list[str]):
    logger.info("creating index")
    fields_array = list(map(lambda x: (x, pymongo.ASCENDING), fields))
    await collection.create_index(fields_array, unique=True)


async def initialize_db_schema():
    await create_unique_constraint(events_collection, ["id"])
