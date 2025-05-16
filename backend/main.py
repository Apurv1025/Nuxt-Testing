from typing import Union
import os
import dotenv

dotenv.load_dotenv()

from fastapi import FastAPI
from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.services.databases import Databases
from appwrite.query import Query

app = FastAPI()


client = Client()
client.set_endpoint(os.getenv("APPWRITE_ENDPOINT"))
client.set_project(os.getenv("APPWRITE_PROJECT"))
client.set_key(os.getenv("APPWRITE_API_KEY"))

users = Users(client)
databases = Databases(client)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/collections")
def get_collections() -> Union[dict, str]:
    """
    Get collections from Appwrite.
    """
    try:
        databases_list = databases.list()
        collections_list = databases.list_collections(
            databases_list["databases"][0]["$id"]
        )
        return {
            "collections": [
                {
                    "$id": collection["$id"],
                    "name": collection["name"],
                    "databaseId": collection["databaseId"],
                }
                for collection in collections_list["collections"]
            ],
        }
    except Exception as e:
        return str(e)


@app.get("/users/search/{starts_with}")
def get_users(starts_with: str) -> Union[dict, str]:
    """
    Get users from Appwrite that start with the given string.
    """
    try:
        if not starts_with:
            starts_with = ""
        db_id = os.getenv("DATABASE_ID")
        if not db_id:
            raise ValueError("DATABASE_ID is not set in environment variables.")
        profiles_collection_id = os.getenv("PROFILES_COLLECTION_ID")
        if not profiles_collection_id:
            raise ValueError(
                "PROFILES_COLLECTION_ID is not set in environment variables."
            )
        response = databases.list_documents(
            db_id,
            profiles_collection_id,
            queries=[
                Query.starts_with("email", starts_with),
                Query.limit(10),
                Query.offset(0),
            ],
        )
        return {
            "total": response["total"],
            "users": [
                {
                    "email": user["email"],
                    "name": user["name"],
                    "userId": user["$id"],
                    "status": user["status"],
                }
                for user in response["documents"]
            ],
        }
    except Exception as e:
        return str(e)


@app.get("/users/{user_id}")
def get_user(user_id: str) -> Union[dict, str]:
    """
    Get user from Appwrite by user ID.
    """
    try:
        db_id = os.getenv("DATABASE_ID")
        if not db_id:
            raise ValueError("DATABASE_ID is not set in environment variables.")
        profiles_collection_id = os.getenv("PROFILES_COLLECTION_ID")
        if not profiles_collection_id:
            raise ValueError(
                "PROFILES_COLLECTION_ID is not set in environment variables."
            )
        response = databases.get_document(
            db_id,
            profiles_collection_id,
            user_id,
        )
        return {
            "email": response["email"],
            "name": response["name"],
            "userId": response["$id"],
            "status": response["status"],
        }
    except Exception as e:
        return str(e)


@app.get("/chatsprofiles/{user_id}")
def get_chatsprofiles(user_id: str) -> Union[dict, str]:
    """
    Get chatsprofiles from Appwrite by user ID.
    """
    try:
        db_id = os.getenv("DATABASE_ID")
        if not db_id:
            raise ValueError("DATABASE_ID is not set in environment variables.")
        profiles_collection_id = os.getenv("PROFILES_COLLECTION_ID")
        if not profiles_collection_id:
            raise ValueError("PROFILES_COLLECTION_ID is not set in environment variables.")
        chatsprofiles_collection_id = os.getenv("CHATSPROFILES_COLLECTION_ID")
        if not chatsprofiles_collection_id:
            raise ValueError(
                "CHATSPROFILES_COLLECTION_ID is not set in environment variables."
            )
        profile = databases.get_document(
            db_id,
            profiles_collection_id,
            user_id,
        )
        if not profile:
            raise ValueError(f"User with ID {user_id} not found.")
        profile.pop("chatsProfiles", None)
        print(profile)
        # TODO: Filter by User ID
        # response = databases.list_documents(db_id,  chatsprofiles_collection_id,
        #     queries= [
        #         Query.contains("profiles",[profile]),
        #         Query.order_desc("latest"),
        #         Query.limit(100000),
        #         Query.offset(0),
        #     ],
        # )
        # return response
    except Exception as e:
        return str(e)
