from beanie import Document as Model
from beanie import PydanticObjectId
from pydantic import BaseModel, Field
from visionguard.common.api_interface.v1.schema.search_engine_user import SearchEngineUser


class DocumentDBBase(SearchEngineUser, Model):

    class Settings:
        name = "user2"
        use_cache = False


Document = DocumentDBBase

