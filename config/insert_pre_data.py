import db
import json

f = open("config/data.json")

data = json.load(f)

for item in data["shoes"]:
    db.collection.insert_one(
        {
            "image": item["image"],
            "name": item["name"],
            "description": item["description"],
            "price": item["price"],
            "color": item["color"]
        }
    )