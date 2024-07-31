from modules import get, json
from auth import client_id

def get_anime_list(offset):
    try:
        with open("./data/anime_data.json", "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    headers = {
        "X-MAL-CLIENT-ID": client_id
        }
    request_uri= f"https://api.myanimelist.net/v2/anime/ranking"
    query = f"?offset={offset}&ranking_type=all&fields=id,title,start_date,mean,rank,popularity,genres(name),num_episodes&limit=500&nsfw=false"
    request = request_uri + query
    result = get(request, headers=headers)
    data = result.json()
    for anime in data["data"]:
        try:
            existing_data.append(anime["node"])
        except:
            pass
    with open("./data/anime_data.json", "w") as f:
        json.dump(existing_data, f, indent=4)
    offset += 500
    if offset < 10000:
        get_anime_list(offset)