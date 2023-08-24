from fastapi import APIRouter

from models.shoes import Shoes
from config.db import conn
from schemas.shoes import shoesEntity, shoesesEntity
from bson import ObjectId

shoes = APIRouter()

@shoes.get("/")
async def get_all_shoeses():
    return shoesesEntity(conn.storedb.shoes.find())

@shoes.get("/{id}")
async def get_shoes(id):
    return shoesEntity(conn.storedb.shoes.find_one({"_id": ObjectId(id)}))

@shoes.post("/")
async def create_new_shoes(shoes:Shoes):
    conn.storedb.shoes.insert_one(dict(shoes))
    return shoesesEntity(conn.storedb.shoes.find())

@shoes.put("/{id}")
async def update_shoes(id, shoes: Shoes):
    conn.storedb.shoes.find_one_and_update({"_id": objectid(id)}, {"$set": dict(shoes)})
    return shoesEntity(conn.storedb.shoes.find_one({"_id": ObjectId(id)}))

@shoes.delete("/{id}")
async def delete_shoes(id, shoes: Shoes):
    return shoesEntity(conn.storedb.shoes.find_one_and_delete({"_id": ObjectId(id)}))
