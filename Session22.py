# Explore Web Crawling:

import pandas as pd
import numpy as np

arr = np.arange(1, 51)
# arr = np.arange(1, 51, 2)
# arr = list(range(1,51))
S1 = pd.Series(arr)
print("--------------")
print(S1)
print("--------------")
print(S1.axes)
# Step is for Indexing
print("--------------")
# print(S1.values)
data = S1.values
print(data)
print(type(data))
print("--------------")
# Head and Tail also works on Pandas Series not only on DataFrame
print(S1.head(5))
print("--------------")
print(S1.tail(5))
print("--------------")

