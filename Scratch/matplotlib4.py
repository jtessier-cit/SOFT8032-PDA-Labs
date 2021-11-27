import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("../dataset/titanic.csv")

labels = ['First Class', 'Second Class', 'Third Class']
bar_width = 0.30
index = np.arange(1, 4)  # [1,2,3]

criteria = df['Survived'] == 0
male = df['Sex'] == 'male'
female = df['Sex'] == 'female'

deadMale = df[criteria & male]
deadFeMale = df[criteria & female]

males = deadMale.groupby("Pclass").size()
females = deadFeMale.groupby("Pclass").size()

plt.bar(index, males, bar_width, color='g')
plt.bar(index+bar_width, females, bar_width, color='b')
plt.xlabel('PClass')
plt.ylabel('Number of Deaths')
plt.title('Titanic Death broken down by PClass and sex')
plt.legend(['Male', 'Female'], loc=2)
plt.xticks(index+0.15, labels)
plt.show()


