def user(item) -> dict:
    return {
        "id": str(item["_id"]),
        "last_name": item["last_name"],
        "first_name": item["first_name"],
        "email": item["email"],
        "created_at": item["created_at"],
        "updated_at": item["updated_at"]
    }