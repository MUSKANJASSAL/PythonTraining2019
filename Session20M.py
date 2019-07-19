# BIG 0 NOTATION

import matplotlib.pyplot as plt
import numpy as np
import math

#X = np.arange(1,101)
X = list(range(1, 101))

# List Comprehension
Y1 = [1 for n in X]
Y2 = [math.log(n) for n in X]
Y3 = [n for n in X]
Y4 = [n*math.log(n) for n in X]
Y5 = [n**n for n in X]
Y6 = [2**n for n in X]
Y7 = [math.factorial(n) for n in X]

plt.xlim(0, 100)
plt.xticks(range(0, 110, 10))
plt.ylim(0,1000)
plt.yticks(np.arange(0,1100,100))

plt.plot(X, Y1, label = "O(1)")
plt.plot(X, Y2, label = "O(logn)")
plt.plot(X, Y3, label = "O(n)")
plt.plot(X, Y4, label = "O(nlogn)")
plt.plot(X, Y5, label = "O(n^2)")
plt.plot(X, Y6, label = "O(2^n)")
plt.plot(X, Y7, label = "O(n!)")

plt.xlabel("Elements")   # X-Axis
plt.ylabel("Operations")   # Y-Axis
plt.title("Polynomial Graphs")  # Title

plt.legend()

plt.show()
