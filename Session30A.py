import numpy as np

# To Create Input Arrays
input1 = np.array([0])
input2 = np.array([1])


class Perceptron:
    theta = 1

    def __init__(self, input, weight):
        # Property of Object and Constructor
        self.input = input
        self.weight = weight

    def activation(self, sum):
        if sum >= Perceptron.theta:
            return 1
        else:
            return 0

    def summation(self):
        s = np.dot(self.input, self.weight)
        y = self.activation(s)
        return y

# Weights for Inputs
# weights = np.array([1, 1])
weights = -1 # AND Operation
# weights = np.array([1.1, 1.1])   # OR Operation

# Define Activation Function and Threshold
# theta = 0
theta = -0.5
def activation(s):   # Binary Unit Step
    if s >= theta:
        return 1
    else:
        return 0

def summation(x, w):
    s = x * w
    y = activation(s)
    return y

output1 = summation(input1, weights)
output2 = summation(input2, weights)

print("For", input1, "|", output1)
print("For", input2, "|", output2)