import numpy as np
import pandas as pd

np.random.seed(12)
s = pd.Series(np.random.rand(10))
# plot the bar chart
s.plot(kind='bar')