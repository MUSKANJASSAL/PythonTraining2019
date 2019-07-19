import pandas as pd
import numpy as np

# List
numbers = [10, 20, 30, 40, 50]

# Numpy Array
array = np.array([11, 22, 33, 44, 55])

print(numbers)
print(array)

# Pandas Series
series = pd.Series([11, 13, 15, 17, 19])
print(series)
print()
# print(series.index)
print()
# print(series.index(11))
print(series.index[1])
# print(series.index[2])
# print(series.index[3])
# print(series.index[4])
#print(series.index[5])
print()
print(pd.Series([1, 2, 3]).array)
print()
ser = pd.Series(pd.Categorical(['a', 'b', 'c']))
print(ser.array)
print()
pd.Series([1, 2, 3]).values
# print(array([1, 2, 3]))