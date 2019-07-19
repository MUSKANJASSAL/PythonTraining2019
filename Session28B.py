# DEEP LEARNING -> PERCEPTRON
#               -> ANN
#               -> NEUTRON
# import numpy as np
# import matplotlib.pyplot as plt
#
# in_array = np.linspace(-np.pi, np.pi, 12)
# out_array = np.tanh(in_array)
#
# print("in_array : ", in_array)
# print("\nout_array : ", out_array)
#
# # red for numpy.tanh()
# plt.plot(in_array, out_array, color='red', marker="o")
# plt.title("numpy.tanh()")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()



import numpy as np
import matplotlib.pylab as plt
def step(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y_step = step(x)
y_sigmoid = sigmoid(x)
y_relu = relu(x)

plt.plot(x, y_step, label='Step', color='k', lw=1, linestyle=None)
plt.plot(x, y_sigmoid, label='Sigmoid', color='k', lw=1, ls='--')
plt.plot(x, y_relu, label='ReLU', color='k', lw=1, linestyle='-.')
plt.ylim(-0.1, 1.1)
plt.legend()
plt.show()