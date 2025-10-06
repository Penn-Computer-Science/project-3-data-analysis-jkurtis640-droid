
import pandas as pd
import random
import matplotlib
## Load our dataframe
df = pd.read_csv('notpandas.csv')
not_pandas_data = pd.DataFrame(df)
print(df.info())

print("-_-_",20)
print("Mean of the Dataframe")
print(not_pandas_data.groupby("Music Genres")['Hours playing videogames'].mean())

print("-_-_",20)
print("Median of the Dataframe")
print(not_pandas_data.groupby("Music Genres")['Hours playing videogames'].median())


print("-_-_",20)
print("Median of the Dataframe")
print(not_pandas_data['Time listening music'].value_counts())

not_pandas_data_sorted = df.sort_values(by='Hours playing videogames')
print(df)