import numpy as np

# To Create Input Arrays
input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

class Perceptron_AND:

    def __init__(self, inputs, weights):
        # Property of Object and Constructor
        self.X = inputs
        self.W = weights

    def activation(self, s):  # Binary Unit Step :)
        self.s = s
        if self.s >= 1:
            return 1
        else:
            return 0

    def summation(self):
        self.S = np.dot(self.X, self.W)
        self.result = self.activation(self.S)
        return self.result

class Perceptron_OR:

    def __init__(self, inputs, weights):
        # Property of Object and Constructor
        self.X = inputs
        self.W = weights

    def activation(self, s):  # Binary Unit Step :)
        self.s = s
        if self.s >= 1:
            return 1
        else:
            return 0

    def summation(self):
        self.S = np.dot(self.X, self.W)
        self.result = self.activation(self.S)
        return self.result

class Perceptron_NOT:

    def __init__(self, inputs, weights):
        # Property of Object and Constructor
        self.X = inputs
        self.W = weights

    def activation(self, s):  # Binary Unit Step :)
        self.s = s
        if self.s >= -0.5:
            return 1
        else:
            return 0

    def summation(self):
        self.S = self.X * self.W
        self.result = self.activation(self.S)
        return self.result


weightsAND = np.array([0.5, 0.5])
weightsOR = np.array([1.1, 1.1])
weightsNOT = -1

# INPUT LAYER
p1_1 = Perceptron_AND(input1, weightsAND).summation()
p1_2 = Perceptron_AND(input2, weightsAND).summation()
p1_3 = Perceptron_AND(input3, weightsAND).summation()
p1_4 = Perceptron_AND(input4, weightsAND).summation()

print(p1_1, p1_2, p1_3, p1_4)

p2_1 = Perceptron_NOT(input1[0], weightsNOT).summation()
p2_2 = Perceptron_NOT(input2[0], weightsNOT).summation()
p2_3 = Perceptron_NOT(input3[0], weightsNOT).summation()
p2_4 = Perceptron_NOT(input4[0], weightsNOT).summation()

print(p2_1, p2_2, p2_3, p2_4)

p3_1 = Perceptron_NOT(input1[1], weightsNOT).summation()
p3_2 = Perceptron_NOT(input2[1], weightsNOT).summation()
p3_3 = Perceptron_NOT(input3[1], weightsNOT).summation()
p3_4 = Perceptron_NOT(input4[1], weightsNOT).summation()

print(p3_1, p3_2, p3_3, p3_4)

# HIDDEN LAYER

p4_1 = Perceptron_AND(np.array([p2_1,p3_1]), weightsAND).summation()
p4_2 = Perceptron_AND(np.array([p2_2,p3_2]), weightsAND).summation()
p4_3 = Perceptron_AND(np.array([p2_3,p3_3]), weightsAND).summation()
p4_4 = Perceptron_AND(np.array([p2_4,p3_4]), weightsAND).summation()

print(p4_1, p4_2, p4_3, p4_4)

# FINAL LAYER

final_1 = Perceptron_OR(np.array([p1_1,p4_1]), weightsAND).summation()
final_2 = Perceptron_OR(np.array([p1_2,p4_2]), weightsAND).summation()
final_3 = Perceptron_OR(np.array([p1_3,p4_3]), weightsAND).summation()
final_4 = Perceptron_OR(np.array([p1_4,p4_4]), weightsAND).summation()

print(final_1,final_2,final_3,final_4)