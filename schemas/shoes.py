def shoesEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "image": item["image"],
        "name": item["name"],
        "description": item["description"],
        "price": item["price"],
        "color": item["color"]
    }

def shoesesEntity(entity) -> list:
    return [shoesEntity(item) for item in entity]