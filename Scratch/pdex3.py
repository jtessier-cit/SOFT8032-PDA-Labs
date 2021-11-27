import numpy as np
import pandas as pd

np.random.seed(19)
s = pd.Series(np.random.rand(10))
s = pd.Series(np.random.rand(10))

# the cumsum function returns a series containing the cumulative sum
# of all values in s
# walk_ts = s.cumsum()
#
# walk_ts.plot()
s.plot(kind='bar')

