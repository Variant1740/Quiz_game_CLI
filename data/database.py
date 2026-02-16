import json
import os
from datetime import datetime

DB_FILE = "leaderboard.json"


def initialize_db():
    if not os.path.exists(DB_FILE):
        default_data={'leaderboard': []}
        with open(DB_FILE, "w") as file:
            json.dump(default_data, file, indent=4)

def load_leaderboard():
    initialize_db()
    with open(DB_FILE, "r") as file:
        data=json.load(file)
        return data["leaderboard"]
    
    
def save_leaderboard(leaderboard_list):
     data={"leaderboard": leaderboard_list}
     with open(DB_FILE, "w") as file:
         json.dump(data, file, indent=4)

