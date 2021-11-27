import matplotlib.pyplot as plt
plt.plot([1,2,3, 4, 5, 6, 7], [1**1, 2**2, 3**3, 4**3, 5**2, 3**3, 4**2])
# (string, xy=(coordinates of pointer), xytext=(coordinates of text), arrowprops=dict(..
plt.annotate('This point in Figure shows ..', xy=(2, 5), xytext=(1, 25),
             arrowprops=dict(arrowstyle="->"))
plt.show()
