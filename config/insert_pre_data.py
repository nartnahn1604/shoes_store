from db import conn
import json

f = open("config/data.json")

data = json.load(f)

for item in data["shoes"]:
    conn.storedb.shoes.insert_one(
        {
            "image": item["image"],
            "name": item["name"],
            "description": item["description"],
            "price": item["price"],
            "color": item["color"]
        }
    )