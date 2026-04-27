def get_username(user_id):
    users = {
        1: "tomas",
        2: "lenka",
        3: "vendulka"
    }
    return users.get(user_id, None)
