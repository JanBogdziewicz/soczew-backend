from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from server.routes.event import EventRouter

from server.database.init import (
    initialize_db_schema
)

import logging

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()


async def cors_exceptions_middleware(request, call_next):
    try:
        return await call_next(request)
    except Exception as err:
        logger.error(err)
        return JSONResponse(
            status_code=500, content={"error": type(err).__name__, "message": str(err)}
        )


app.middleware("http")(cors_exceptions_middleware)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(EventRouter, tags=["Event"], prefix="/events")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "hello"}


@app.on_event("startup")
async def startup():
    await initialize_db_schema()
