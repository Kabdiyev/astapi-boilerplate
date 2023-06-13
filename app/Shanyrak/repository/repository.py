from typing import Any

from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult


class PostRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_post(self, user_id, post):
        payload = {
            "user_id": ObjectId(user_id),
            "type": post["type"],
            "address": post["address"],
            "rooms": post["rooms"],
            "phone": post["phone"],
        }

        self.database["posts"].insert_one(payload)

    def get_post(self, user_id: str):
        posted = self.database["posts"].find(
            {
                "user_id": ObjectId(user_id),
            }
        )
        result = []
        for pos in posted:
            result.append(pos)

        return result

    def update_post(self, _id: str, user_id: str, data: dict[str, Any]) -> UpdateResult:
        return self.database["posts"].update_one(
            filter={"_id": ObjectId(_id), "user_id": ObjectId(user_id)},
            update={
                "$set": data,
            },
        )

    def delete_post(self, _id: str, user_id: str) -> DeleteResult:
        return self.database["posts"].delete_one(
            {"_id": ObjectId(_id), "user_id": ObjectId(user_id)}
        )
