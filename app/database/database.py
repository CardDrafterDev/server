def get_user_inventory(user_id: int) -> list[str]: # mock for now
    inventories = {
        2: ["c_002", "c_003", "c_001"],
        3: ["c_003", "c_005"]
    }
    return inventories.get(user_id, None)


def get_user_collection(user_id: int) -> list[str]:
    inventories = {
        2: ["c_002", "c_003", "c_001", "c_015"],
        3: ["c_003", "c_005", "c_016"]
    }

    return inventories.get(user_id, None)