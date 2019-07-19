import pandas as pd
import numpy as np

# List of positive numbers only
data = np.random.rand(5, 4)
# List of positive and negative numbers both
# data = np.random.randn(5, 4)
print(data)

frame = pd.DataFrame(data, columns=["COL1", "COL2", "COL3", "COL4"])
print(frame)
print("------------")
print(frame["COL1"])
print("------------")
# Iterate using iteritems functions: Columns
for key, value in frame.iteritems():
    # print(key, "|", value)
    print(key)
    print("-------")
    print(value)
    print(type(value))
    print(">>>>>>>>>>>")

# Conclusion: DataFrame is collection of Series
#             Series is a collection of numpy ndarray

print("===========================================")

# Iterate using iterrows functions: Rows
for key, value in frame.iterrows():
    # print(key, "|", value)
    print(key)
    print("-------")
    print(value)
    print(type(value))
    print(">>>>>>>>>>>")


print("===========================================")

#  Iterate using itertuples functions: Return Rows as a Tuple
for row in frame.itertuples():
    # print(key, "|", value)
    print(row)
    print(">>>>>>>>>>>")

