import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")
flt = df [[ 'Age']]
y = flt[['Age']]
y = y.dropna()
y1 = y.values
print(len((list(y1))))
enc = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
#print(X)
enc.fit(y1)
y1 = (enc.transform(y1))
print(len(list(y1)))
newDF = pd.DataFrame({"before": list(y.values), "after": list(y1)})
print(newDF.head(200).to_string())
print(newDF['after'].apply(lambda x: int(x)).unique())
print(type(newDF['after'].apply(lambda x: int(x)).unique()))

df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")
flt = df [[ 'Fare']]
y = flt[['Fare']]
y = y.dropna()
y1 = y.values
print(len((list(y1))))
enc = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
#print(X)
enc.fit(y1)
print(enc.bin_edges_)
y1 = (enc.transform(y1))
print(len(list(y1)))
newDF = pd.DataFrame({"before": list(y.values), "after": list(y1)})
print(newDF.head(20))
print(newDF['after'].value_counts())

# print(newDF.info())