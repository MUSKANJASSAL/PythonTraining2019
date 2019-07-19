import numpy as np

# To Create Input Arrays
input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

# Weights for Inputs
# weights = np.array([1, 1])
weights = np.array([0.5, 0.5]) # AND Operation
# weights = np.array([1.1, 1.1])   # OR Operation

# AND | OR
class Perceptron:

    theta = 1

    def __init__(self, inputs, weights):
        # Property of Object and Constructor
        self.inputs = inputs
        self.weights = weights

    def activation(self, sum):
        if sum >= Perceptron.theta:
            return 1
        else:
            return 0

    def summation(self):
        s = np.dot(self.inputs, self.weights)
        y = self.activation(s)
        return y


model = Perceptron(input1, weights)
# model = Perceptron(input2, weights)
# model = Perceptron(input3, weights)
# model = Perceptron(input4, weights)


output = model.summation()

print("For",input1,"|",output)
