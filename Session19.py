import numpy as np

arr1 = np.arange(10, 21)
print(arr1)
print(arr1.ndim)

print()

arr2 = np.arange(10, 31, 3)
print(arr2)

print()

arr3 = np.ones((3,3))       # 2D Array
print(arr3, type(arr3))

print()

arr4 = np.ones((3,3,3), dtype=int)
print(arr4)

print()

arr5 = np.ones((3,3), dtype=int)
arr5[0][1] = 9
print(arr5)

print()

arr6 = np.linspace(0, 21, 4)   # Divide into 4
print(arr6)


print("Num Arrays!!")

X=np.array([[1,0],[0,1]])
print(X)
print(type(X))
print(X.ndim)
Y=np.array([2,3,1,8])
print(Y)
print(type(Y))
print(Y.ndim)