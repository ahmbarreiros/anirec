
def format_mal_data(data):
    formatted_data = dict()
    formatted_data.setdefault("Id", [])
    formatted_data.setdefault("Title", [])
    formatted_data.setdefault("Picture", [])
    formatted_data.setdefault("Start_Date", [])
    formatted_data.setdefault("Mean_Score", [])
    formatted_data.setdefault("Rank", [])
    formatted_data.setdefault("Popularity", [])
    formatted_data.setdefault("genre_1_id", [])
    formatted_data.setdefault("genre_2_id", [])
    formatted_data.setdefault("genre_3_id", [])
    formatted_data.setdefault("genre_1", [])
    formatted_data.setdefault("genre_2", [])
    formatted_data.setdefault("genre_3", [])
    # formatted_data.setdefault("Genres_Id", [])
    # formatted_data.setdefault("Genres", [])
    formatted_data.setdefault("Num_of_Episodes", [])
    formatted_data.setdefault("Media_Type", [])
    formatted_data.setdefault("P_Status", [])
    formatted_data.setdefault("P_Score", [])
    # formatted_data.setdefault("P_Completion", [])
    # formatted_data.setdefault("P_Episodes_Watched", [])
    for element in data:
        formatted_data["Id"].append(element["node"]["id"])
        formatted_data["Title"].append(element["node"]["title"])
        formatted_data["Picture"].append(element["node"]["main_picture"]["medium"])
        try:
            formatted_data["Start_Date"].append(element["node"]["start_date"])
        except:
            formatted_data["Start_Date"].append(None)
        try:
            formatted_data["Mean_Score"].append(element["node"]["mean"])
        except:
            formatted_data["Mean_Score"].append(None)
        try:
            formatted_data["Rank"].append(element["node"]["rank"])
        except:
            formatted_data["Rank"].append(None)
        formatted_data["Popularity"].append(element["node"]["popularity"])
        try:
            formatted_data["genre_1_id"].append((element["node"]["genres"][0]["id"]))
            formatted_data["genre_1"].append((element["node"]["genres"][0]["name"]))
        except:
            formatted_data["genre_1_id"].append(-1)
            formatted_data["genre_1"].append("Unkown")
        try:
            formatted_data["genre_2_id"].append((element["node"]["genres"][1]["id"]))
            formatted_data["genre_2"].append((element["node"]["genres"][1]["name"]))
        except:
            formatted_data["genre_2_id"].append(-1)
            formatted_data["genre_2"].append("Unkown")
        try:
            formatted_data["genre_3_id"].append((element["node"]["genres"][2]["id"]))
            formatted_data["genre_3"].append((element["node"]["genres"][2]["name"]))
        except:
            formatted_data["genre_3_id"].append(-1)
            formatted_data["genre_3"].append("Unkown")
        # formatted_data["Genres_Id"].append(format_genres_id_from_mal(element["node"]["genres"]))
        # formatted_data["Genres"].append(format_genres_from_mal(element["node"]["genres"]))
        formatted_data["P_Status"].append(element["list_status"]["status"])
        formatted_data["P_Score"].append(element["list_status"]["score"])
        formatted_data["Num_of_Episodes"].append(element["node"]["num_episodes"])
        formatted_data["Media_Type"].append(element["node"]["media_type"])
        # formatted_data["P_Episodes_Watched"].append(element["list_status"]["num_episodes_watched"])
    return formatted_data

def format_genres_from_mal(genres):
    new_genres = list()
    for genre in genres:
        new_genres.append(genre["name"])
    return new_genres
def format_genres_id_from_mal(genres_ids):
    new_genres = list()
    for genre in genres_ids:
        new_genres.append(genre["id"])
    return new_genres
