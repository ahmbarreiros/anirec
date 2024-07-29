from get_anime_list import get_anime_list

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = get_anime_list("toinMAL")

def format_mal_data(data):
    formatted_data = dict()
    formatted_data.setdefault("Title", [])
    formatted_data.setdefault("Picture", [])
    formatted_data.setdefault("Start Date", [])
    formatted_data.setdefault("Mean Score", [])
    formatted_data.setdefault("Rank", [])
    formatted_data.setdefault("Popularity", [])
    formatted_data.setdefault("Genres", [])
    formatted_data.setdefault("Num. of Episodes", [])
    formatted_data.setdefault("Status", [])
    formatted_data.setdefault("Score", [])
    formatted_data.setdefault("Episodes Watched", [])
    for element in data:
        formatted_data["Title"].append(element["node"]["title"])
        formatted_data["Picture"].append(element["node"]["main_picture"]["medium"])
        try:
            formatted_data["Start Date"].append(element["node"]["start_date"])
        except:
            formatted_data["Start Date"].append(None)
        try:
            formatted_data["Mean Score"].append(element["node"]["mean"])
        except:
            formatted_data["Mean Score"].append(None)
        try:
            formatted_data["Rank"].append(element["node"]["rank"])
        except:
            formatted_data["Rank"].append(None)
        formatted_data["Popularity"].append(element["node"]["popularity"])
        formatted_data["Genres"].append(format_genres_from_mal(element["node"]["genres"]))
        formatted_data["Num. of Episodes"].append(element["node"]["num_episodes"])
        formatted_data["Status"].append(element["list_status"]["status"])
        formatted_data["Score"].append(element["list_status"]["score"])
        formatted_data["Episodes Watched"].append(element["list_status"]["num_episodes_watched"])
    return formatted_data

def format_genres_from_mal(genres):
    new_genres = list()
    for genre in genres:
        new_genres.append(genre["name"])
    return new_genres

formatted_data = format_mal_data(data)
df = pd.DataFrame.from_dict(formatted_data)
print(len(df))
genres_dummies = pd.get_dummies(df["Genres"].apply(pd.Series).stack()).sum()
print(genres_dummies)
print(len(genres_dummies))
# df = pd.concat([df, genres_dummies], axis=1)
# print(len(df))
# print(df["Genres"])
# print(df.info())
# print(df.describe())