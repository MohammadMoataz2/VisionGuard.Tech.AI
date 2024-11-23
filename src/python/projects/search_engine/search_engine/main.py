import sys

from dns.resolver import query

vision_guard_path = "/home/sheildsword2/Desktop/Work/DataEng/VisionGuard.Tech.AI.SearchEngine/src/python/libs/common/"
sys.path.append(vision_guard_path)



from visionguard.common.api_interface.v1.schema.search_engine_user import (

    SearchEngineUser,
    SearchEngineUserResultQuery,
    SearchEngineUserQuery,
    SearchEngineResultQuery,
    SearchEngineResult,
    SearchEngineQuery
)
from visionguard.common.api_interface.v1.schema.search_engine_query import SearchEngineQueryBs4Google



user_attributes = {
    "age": 20,
    "race": "asian",
    "gender": "Man",
    "emotion": "happy"
}

user_attributes_other = {
    "location": "jordan"
}

user_obj = SearchEngineUser(
    user_attributes = user_attributes,
    user_attributes_other = user_attributes_other,

                            )





print("This is The User Object", user_obj)



search_result = SearchEngineQueryBs4Google()




user_obj.user_query_result.append(SearchEngineUserResultQuery(

    user_query=SearchEngineUserQuery(
     query_obj= search_result
    ),

    result_query=SearchEngineResultQuery(

            query_result= search_result.search(),
    )

)
)
print(user_obj)




