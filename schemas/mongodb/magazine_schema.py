def individual_serial(magazine) -> dict:
    return {
        "id": str(magazine["_id"]),
        "tag_number": magazine["tag_number"],
        "thumbnail": magazine["thumbnail"],
        "main_photo": magazine["main_photo"],
        "title": magazine["title"],
        "photos": magazine["photos"],
        "content": magazine["content"],
        "related_place_tags": magazine["related_place_tags"]
    }

def list_serial(magazines) -> list:
    return [individual_serial(magazine) for magazine in magazines]
