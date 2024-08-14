def individual_serial(post) -> dict:
    return {
        "id": str(post["_id"]),
        "island_tag_number": post["island_tag_number"],
        "place_tag_number": post["place_tag_number"],
        "user_id": post["user_id"],
        "photos": post["photos"],
        "keywords": post["keywords"],
        "rating": post["rating"],
        "review": post["review"]
    }

def list_serial(posts) -> list:
    return [individual_serial(post) for post in posts]
