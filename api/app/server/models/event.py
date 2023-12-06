from pydantic import BaseModel, Field, validator


class EventSchema(BaseModel):
    name: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "BOTO Noise",
            }
        }


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }
