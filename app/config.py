from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()
uri=os.getenv("MONGO_URL")

# Create a new client and connect to the server
client = AsyncIOMotorClient(uri)
db=client.Todo_DB
collection=db["todo"]