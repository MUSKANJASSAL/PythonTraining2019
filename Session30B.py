# BIAS
import numpy as np

# To Create Input Arrays
input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

# Weights for Inputs
weights = np.array([1, 1])

# Define Activation Function and Threshold
theta = 0
def activation(s):   # Binary Unit Step
    if s >= theta:
        return 1
    else:
        return 0

def summation(x, w, b):
    s = np.dot(x, w) + b
    y = activation(s)
    return y

# bias = -1.5  # AND
# bias = -1      # OR
bias = -0.     # OR
output1 = summation(input1, weights, bias)
output2 = summation(input2, weights, bias)
output3 = summation(input3, weights, bias)
output4 = summation(input4, weights, bias)

print("For", input1, "|", output1)
print("For", input2, "|", output2)
print("For", input3, "|", output3)
print("For", input4, "|", output4)