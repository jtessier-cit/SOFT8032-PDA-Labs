import random
import numpy as np
import time

startPython = int(round(time.time() * 1000))

a = list(range(10_000_000))
b = list(range(10_000_000))
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
stopPython = int(round(time.time() * 1000))
pythonTime = stopPython - startPython

startPython2 = int(round(time.time() * 1000))

d = []
for i in range(10000000):
    d.append(i + i)

stopPython2 = int(round(time.time() * 1000))
pythonTime2 = stopPython2 - startPython2
print(pythonTime2)

startNumPy = int(round(time.time() * 1000))
a = np.arange(10000000, dtype=int)
b = np.arange(10000000, dtype=int)
c = a+b
stopNumPy = int(round(time.time() * 1000))
numpyTime = stopNumPy - startNumPy

startNumPy2 = int(round(time.time() * 1000))
a = np.arange(10000000, dtype=int)

c = a+a
stopNumPy2 = int(round(time.time() * 1000))
numpyTime2 = stopNumPy2 - startNumPy2
print(numpyTime2)

print(f"{pythonTime}\t{numpyTime}")
print(numpyTime/pythonTime)
