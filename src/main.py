from get_anime_list import get_anime_list
from format_mal_data import format_mal_data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = get_anime_list("toinMAL")
# data = get_anime_list("Alves_Gabriel")

formatted_data = format_mal_data(data)

df = pd.DataFrame.from_dict(formatted_data)

X = df.drop(["Title", "Picture", "Start_Date", "P_Score", "genre_1", "genre_2", "genre_3"], axis=1).values
y = df["P_Score"].values

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [-1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
y = y.reshape(len(y), 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

sc_x = StandardScaler()
sc_y = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)
y_train = sc_y.fit_transform(y_train)
y_test = sc_y.transform(y_test)

print(X_train)
print(y_train)


# all_genres = pd.Series(df[['genre_1', 'genre_2', 'genre_3']].values.ravel()).unique()
# print(all_genres)