import numpy as np

# load the data with NumPy function loadtxt
# Load data from a text file. Each row in the text file must have the same number of values.
arr = np.loadtxt("data.txt")
print(arr)

print("=============")

# 1-D Array | Try out 2D and 3D Arrays as well

arr = np.arange(10, 200, 10)
print(arr)
#np.savetxt("arraydata.txt", arr)  # Default
np.savetxt("arraydata.txt", arr, fmt="%04d", delimiter=",")  # 4->for four spaces d->for integer
# Delimiter-> Separated by Commas
print("==Data Written==")
np.loadtxt