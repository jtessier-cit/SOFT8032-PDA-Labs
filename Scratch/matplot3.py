import pandas as pd
import matplotlib.pyplot as plt

# read in a dataset
df = pd.read_csv("../dataset/titanic.csv")

# filter the dataframe to only return rows where the passenger died
criteria = df['Survived']==0
fatalities = df[criteria]
pclassGroup = fatalities.groupby("Pclass")

# extract the Survived column from the groupby object
classSurived = pclassGroup['Survived'].count()
print(classSurived)
classSurived.plot()
labels = ['First Class', 'Second Class', 'Third Class']
plt.xticks([1, 2, 3], labels)
plt.show()