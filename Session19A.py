import numpy as np

# Explore: asarray vs array ;)

arr = np.arange(10, 51, 3)
print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)  # n Dimensional

# Access Array Elements
print(arr[1])
print(arr[-1])

# Slicing
print(arr[:3])
print(arr[-2:-7:-1])
print(arr[3:5])
print(arr[-5])

slices = slice(1, 20, 2)
print(slices)
print(arr[slices])

arr2D = np.array([(1, 2, 3), (3, 4, 5), (6, 7, 8)])
print(arr2D)
print(arr2D.shape)
print(arr2D.ndim)

print(arr2D[0][1])   # 2

print("**************")

print(arr2D[0:2])   # (1, 2, 3), (3, 4, 5)

print("**************")

print(arr2D[0][1])
print(arr2D[0, 1])   # 2

print(arr2D[0:2 , 0:2])

print()

print(arr2D[1:, 1:])

print()

arr3D = np.array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],
       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],
       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])

print(arr3D)
print(type(arr3D))
print(arr3D.ndim)
print(arr3D.shape)

print()

print(arr3D[0][0][0])
print(arr3D[0][0][1])
print(arr3D[0][0][2])

print()

print(arr3D[0][1][0])
print(arr3D[0][1][1])
print(arr3D[0][1][2])

print()

print(arr3D[0][2][0])
print(arr3D[0][2][1])
print(arr3D[0][2][2])

print()

print(arr3D[1][0][0])
print(arr3D[1][0][1])
print(arr3D[1][0][2])

print()

print(arr3D[1][1][0])
print(arr3D[1][1][1])
print(arr3D[1][1][2])

print()

print(arr3D[1][2][0])
print(arr3D[1][2][1])
print(arr3D[1][2][2])

print()

print(arr3D[2][0][0])
print(arr3D[2][0][1])
print(arr3D[2][0][2])

print()

print(arr3D[2][1][0])
print(arr3D[2][1][1])
print(arr3D[2][1][2])

print()

print(arr3D[2][2][0])
print(arr3D[2][2][1])
print(arr3D[2][2][2])

# Slicing
print()

print(arr3D[0:2])

print()

print(arr3D[1:, 1:])