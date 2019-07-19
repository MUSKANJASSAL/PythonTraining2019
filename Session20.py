# Code Data Analysis and Machine Learning Online
# https://jupyter.org/try
import pandas as pd

numbers = [10, 20, 30, 40, 50]
ages = {"John":30, "Jennie":26, "Jim":12, "Jack":22, "Joe":33}

s1 = pd.Series(numbers)
s2 = pd.Series(ages)

print(s1)
print()
print(s2)
print()
s2 = pd.Series(ages)
print(s2)

print("============")

# Access Elements in Series by Indexing

print(s1[1])
print(s2["John"])

# Slicing in Series

print(s1[1:])
print(s1[:3])
print(s1[2:5])

print("===========")

print(s2["Jennie":])
print(s2[:"Jim"])
print(s2["Jennie":"Joe"]) #  jennie and joe will be inclusive