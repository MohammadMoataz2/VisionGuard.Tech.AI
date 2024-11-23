from beanie import Document as Model
from beanie import PydanticObjectId
from visionguard.common.api_interface.v1.schema.search_engine_user import SearchEngineUser


class DocumentDBBase(SearchEngineUser, Model):
    class Settings:
        name = "user"


Document = DocumentDBBase

