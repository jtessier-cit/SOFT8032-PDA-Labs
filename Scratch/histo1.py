import matplotlib.pyplot as plt
import numpy as np
gaussian_numbers = np.random.normal(size=1000)
plt.hist(gaussian_numbers, bins=40)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# create a histogram
np.random.seed(10)
# 1000 random numbers
dfh = pd.DataFrame(np.random.rand(1000))
# draw the histogram
dfh.hist(bins=30);
