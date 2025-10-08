
import pandas as pd
import random
import matplotlib.pyplot as plt
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

not_pandas_data.groupby('Time listening music')["Hours playing videogames"].mean().plot(kind="bar")
plt.show()

plt.hist(not_pandas_data, bins=10, edgecolor='blue')
# Creates the histogram
plt.ylabel("time listening to music")
# labeling the x axis
plt.xlabel("hours playing videogames")
# labeling the y axis
plt.title("Time listening to music vs Hours playing videogames")
# Does the title
plt.legend()
plt.show()

fig, ax = plt.subplots()
# figure and axis allows to plot a line
for name, group in df.groupby('Hours playing videogames'):
# allows the ability to group the line plot seperately
    group.plot(x='Time listening music',y='Hours playing videogames',label='name',ax=ax,kind='line')
    # Sets the parameters of the line plot

ax.set_title("hours playing videogames vs time listening music")
ax.set_xlabel("Time listening music")
ax.set_ylabel("Hours playing videogames")
ax.legend()
plt.show()