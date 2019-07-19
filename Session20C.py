# Matplotlib is a Python 2D plotting library
import matplotlib.pyplot as plt

"""
    X: 0,  1,  2,  3,  4
    Y: 10, 20, 30, 40, 50
"""

# Assuming X Axis will be indexes
# Y = [10, 40, 300, 1800, 90]
# plt.plot(Y)
# plt.show()

X = [1, 2, 3, 4, 5]

# List Comprehension
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

print(X)
print(Y1)
print(Y2)
print(Y3)

plt.plot(X, Y1, label = "Y1")
plt.plot(X, Y2, label = "Y2")
plt.plot(X, Y3, label = "Y3")

plt.legend()

plt.show()

# Positioning of legend can be changed. Explore ;)

plt.xlabel("X-Axis")   # X-Axis
plt.ylabel("Y-Axis")   # Y-Axis
plt.title("Polynomial Graphs")  # Title
plt.grid(True)

# plt.xlim(0, 100)
# plt.ylim(0, 1000)

# plt.savefig("MyGraph")
plt.show()