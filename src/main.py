from get_anime_list import get_anime_list

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = get_anime_list("toinMAL")
# data = get_anime_list("Alves_Gabriel")
print(data)
def format_mal_data(data):
    formatted_data = dict()
    formatted_data.setdefault("Title", [])
    formatted_data.setdefault("Picture", [])
    formatted_data.setdefault("Start_Date", [])
    formatted_data.setdefault("Mean_Score", [])
    formatted_data.setdefault("Rank", [])
    formatted_data.setdefault("Popularity", [])
    formatted_data.setdefault("genre_1", [])
    formatted_data.setdefault("genre_2", [])
    formatted_data.setdefault("genre_3", [])
    formatted_data.setdefault("Num_of_Episodes", [])
    formatted_data.setdefault("P_Status", [])
    formatted_data.setdefault("P_Score", [])
    formatted_data.setdefault("P_Episodes_Watched", [])
    for element in data:
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
            formatted_data["genre_1"].append((element["node"]["genres"][0]["name"]))
        except:
            formatted_data["genre_1"].append(None)
        try:
            formatted_data["genre_2"].append((element["node"]["genres"][1]["name"]))
        except:
            formatted_data["genre_2"].append(None)
        try:
            formatted_data["genre_3"].append((element["node"]["genres"][2]["name"]))
        except:
            formatted_data["genre_3"].append(None)
        formatted_data["Num_of_Episodes"].append(element["node"]["num_episodes"])
        formatted_data["P_Status"].append(element["list_status"]["status"])
        formatted_data["P_Score"].append(element["list_status"]["score"])
        formatted_data["P_Episodes_Watched"].append(element["list_status"]["num_episodes_watched"])
    return formatted_data

formatted_data = format_mal_data(data)
df = pd.DataFrame.from_dict(formatted_data)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.head(1))