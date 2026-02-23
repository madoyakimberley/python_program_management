import json
import os
from models.user import User

DATA_FILE = "data/data.json"


def save_data(data):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_users(users):
    data = [user.to_dict() for user in users]
    save_data({"users": data})


def load_users():
    data = load_data()

    users = []

    if isinstance(data, dict) and "users" in data:
        user_list = data["users"]

    elif isinstance(data, list):
        user_list = data

    else:
        user_list = []

    for user_data in user_list:
        users.append(User.from_dict(user_data))

    return users