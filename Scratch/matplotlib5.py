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

# plt.bar(index, males, bar_width, color='g')
# plt.bar(index+bar_width, females, bar_width, color='b')


plt.plot(index, males)
plt.plot(index, females)
plt.xticks(index)
plt.xlabel('Passenger Class')
plt.ylabel('Number of Fatalities')
plt.title('Males and Females Fatalities By Class deaths')
plt.annotate('Dramatic rise in male third class', xy=(2.5, 200),
             xytext=(1.4, 230), arrowprops=dict(arrowstyle="->"))
plt.legend(['Male', 'Female'], loc = 2)
plt.show()