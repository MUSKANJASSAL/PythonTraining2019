# Problem 1. -> Cyclic	Rotation:
# Shift	the	elements of	Multi Value Container A	to the right with R	shifts

A = [3,8,9,7,6]
B = 3
for i in range(B):
    C = A.pop()
    A.insert(0,C)
print("Its the answer after doing",B,"right shift: ",A)
print()
print("********************************")
"""
R = 3
list_1 = [3, 8, 9, 7, 6]
list_1 = (list_1[-n:] + list_1[:-n])
print(list_1)

print(list_1)
print("********************************")
def rotate(A, n):
   x = A[n - 1]
   for i in range(n - 1, 0, -1):
      A[i] = A[i - 1];
   A[0] = x;
# Driver function
A=list()
n=int(input("Enter the size of the List :"))
print("Enter the Element of  List :")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
print ("The array is ->")
for i in range(0, n):
   print (A[i], end = ' ')
rotate(A, n)
print ("\nRotated array is")
for i in range(0, n):
   print (A[i], end = ' ')
"""
# Problem 2. ->
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
M = 4
D = [0]
X = 0
while X != len(A):
    # print(A)
    for i in range(M):
        C = A.pop(0)
        A.insert(len(A),C)
    D.append(A[0])
    X += 1
# print(D)
# print(set(D))
print(len(set(D)))

# Prpblem 3. ->
def maxHandshake(n):
    return int((n * (n - 1)) / 2)
n = 10
print(maxHandshake(n))