# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(365, 2), index=pd.date_range('2014-01-01', '2014-12-31'),columns=list('AB'))

walk_df = df.cumsum()
walk_df.plot()
walk_df.head()
plt.show()

