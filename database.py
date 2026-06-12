from motor.motor_asyncio import AsyncIOMotorClient
from mongomock_motor import AsyncMongoMockClient
from dotenv import load_dotenv
import os

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "false").lower() == "true"

if USE_MOCK:
    client = AsyncMongoMockClient()
    db = client.get_database("test")
else:
    client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    db = client.get_default_database()

database = db["avaliacoes"]
