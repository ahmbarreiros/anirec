from get_user_anime_list import get_user_anime_list
from get_anime_list_data import get_anime_list_data
from format_mal_data import format_mal_data
from modules import *

# import tensorflow as tf
from get_max_genre_id import get_max_genre_id

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

anime_list_data = get_anime_list_data()

data = get_user_anime_list("toinMAL")
# data = get_user_anime_list("Alves_Gabriel")

formatted_data = format_mal_data(data)

df = pd.DataFrame.from_dict(formatted_data)

X = df.drop(["Title", "Picture", "Start_Date", "P_Score", "genre_1", "genre_2", "genre_3"], axis=1).values
y = df["P_Score"].values
le = LabelEncoder()
X[:, 8] = le.fit_transform(X[:, 8])
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [-1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
X = imputer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=.2)

sc_x = StandardScaler()
sc_y = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)
y_train = sc_y.fit_transform(y_train.reshape(len(y_train), 1)).flatten()
y_test = sc_y.transform(y_test.reshape(len(y_test), 1)).flatten()

