from modules import get, json
from auth import client_id

def get_user_anime_list(user_name):
    headers = {
        "X-MAL-CLIENT-ID": client_id
        }
    request_uri= f"https://api.myanimelist.net/v2/users/{user_name}/animelist"
    query = "?sort=list_score&fields=id,title,start_date,mean,rank,popularity,genres(name),num_episodes,media_type,list_status(status, score, num_episodes_watched)&limit=1000&nsfw=false"
    request = request_uri + query
    result = get(request, headers=headers)
    data = result.json()
    return data["data"]

def get_next_page(request):
    headers = {
        "X-MAL-CLIENT-ID": client_id
        }
    result = get(request, headers=headers)
    data = result.json()
    return data
