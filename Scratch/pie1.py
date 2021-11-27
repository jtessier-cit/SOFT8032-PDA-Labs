import matplotlib.pyplot as plt
import numpy as np

labels = 'FF', 'FG', 'Labour', 'Sin Fein'
# Interviewed 829 people about first choice political party
popularity = [220, 248, 216, 145]
sectionToExplode=(0, 0.1, 0, 0)
plt.pie(popularity, explode=sectionToExplode, labels=labels,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Popular Political Parties')
plt.show()
