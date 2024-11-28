from beanie import Document as Model
from beanie import PydanticObjectId
from pydantic import BaseModel, Field
from api.api_interface.v1.schema import SearchEngineUser


class DocumentDBBase(SearchEngineUser, Model):

    class Settings:
        name = "user2"



Document = DocumentDBBase

