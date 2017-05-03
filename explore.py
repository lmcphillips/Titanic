import pandas as pd

from urllib.request import urlretrieve

url = 'https://kaggle2.blob.core.windows.net/competitions-data/kaggle/3136/train.csv'

#save file locally
urlretrieve(url, 'titanic.csv')

titanic = pd.read_csv('titanic.csv')

print(titanic.head())


