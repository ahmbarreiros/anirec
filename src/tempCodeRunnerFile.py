from get_anime_list import get_anime_list

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = get_anime_list("toinMAL")
# data = get_anime_list("Alves_Gabriel")
print(data)