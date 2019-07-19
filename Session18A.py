import numpy as np
import time

stamp1 = time.time()

arr1 = np.array([10, 20, 30, 40, 50])

arr2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# arr3 np.array([[[], []]])

print(arr1)
print(len(arr1))
print(arr1[1])   # 20

print()

print(arr2)
print(len(arr2))
print(arr2[1][2])   # 60

a1 = np.zeros(8)
print(a1)
print(a1.shape)
"""
a1 = np.ones(8)
print(a1)

print(a1.shape)
"""

a2 = a1.reshape(2, 2, 2)
print(a1)
print(a2)

a3 = a2.ravel()   # Revert back to Original
print(a3)

stamp2 = time.time()

print("Difference:",stamp2-stamp1)