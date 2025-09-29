from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import os
import datetime 

app = FastAPI()
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASSWORD")
MONGO_DB   = os.getenv("MONGO_DB")

MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASS}@mongo:27017/{MONGO_DB}?authSource=admin"
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

class Lead(BaseModel):
    id: int
    company_name: str
    location: str
    size: int
    industry: str
    recent_news: str
    outreach_hook: str
    date_added: datetime.datetime.now()


@app.get("/")
def getCollections():
    return {"lol": base}
