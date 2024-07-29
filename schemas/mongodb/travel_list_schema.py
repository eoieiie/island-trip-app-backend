def individual_serial(travel_list) -> dict:
    return {
        "id": str(travel_list["_id"]),
        "user_id": travel_list["user_id"],
        "travel_name": travel_list["travel_name"],
        "island_tag_number": travel_list["island_tag_number"],
        "start_date": travel_list["start_date"],
        "end_date": travel_list["end_date"],
        "daily_plans": travel_list["daily_plans"]
    }

def list_serial(travel_lists) -> list:
    return [individual_serial(travel_list) for travel_list in travel_lists]
