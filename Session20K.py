import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2, 100)
#
# plt.plot(x, x, label='linear')
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')
#
# plt.xlabel('x label')
# plt.ylabel('y label')
#
# plt.title("Simple Plot")
#
# plt.legend()
#
# plt.show()

x = np.arange(0, 10, 0.2)
#y = np.sin(x)
#y = np.cos(x)
y = np.tan(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

print("=====================")

plt.plot([1, 2, 3, 4])
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

plt.ylabel('some numbers')
plt.show()

print("==================")

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()