# NUMERICAL PYTHON
# https://www.numpy.org/
import numpy as np

# List Creation
numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers))

"""
# array = np.array(10, 20, 30, 40, 50)  # only 2 non-keyword arguments accepted
array = np.array([10, 20, 30, 40, 50])
print(array, type (array))
array = np.array({10, 20, 30, 40, 50})
print(array, type (array))
array = np.array((10, 20, 30, 40, 50))
print(array, type (array))
dict = {"eid":101, "ename":"John", "salary":10000}
array = np.array(dict)
print(array, type(array))
"""

print()

# Pass List/Tuple/Set/Dictionary/String i.e. all the sequences

array = np.array([10, 20, 30, 40, 50])
print(array, type(array))

# Check Size
print(len(array))

print()

# Update Data in Array
array[2] = 222

array2 = np.append(array, [11, 12, 13])
print(array2)

# Iterate in Array
for elm in array:
    print(elm)