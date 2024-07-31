from modules import json, os

def get_anime_list_data():
    try:
        with open("./data/anime_data.json", "r") as f:
                anime_list_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        from get_anime_list import get_anime_list
        if os.path.exists("./data/anime_data.json"):
            os.remove("./data/anime_data.json")
        get_anime_list(0)
        with open("./data/anime_data.json", "r") as f:
            anime_list_data = json.load(f)
    return anime_list_data
