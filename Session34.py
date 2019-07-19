import torch
import numpy as np

print(">> Torch Version:", torch.__version__)

# Construct a 5x3 matrix,
X = torch.empty(5, 3)   # 5 Arrays with 3 Elements
print(X)
print(type(X))  # Tensor -> N-D Array in PyTorch and TensorFlow

print()

# Construct a randomly initialized matrix
X = torch.rand(3, 3)
print(X)

print()

X = torch.zeros(5, 5)
print(X)

print()

#  Construct a matrix filled zeros and of dtype long
X = torch.zeros(5, 5, dtype=torch.int)
print(X)

print()

# Start Exploring: https://pytorch.org/tutorials/
# Explore: https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py

print()

# Construct a tensor directly from data:
X = torch.tensor([5.5, 3])
print(X)

# Get its size:
print(X.size())

print()

# Python List
numbers = [10, 20, 30, 40, 50]

# Creating a PyTorch Tensor from Python List
torchTensor = torch.tensor(numbers)
print(torchTensor)

ndArr = torchTensor.numpy()
print(ndArr)

# Convert numpy Array to PyTorch Tensor
data = np.array([1, 3, 5, 7, 9])
print(data)

torchData = torch.from_numpy(data)
print(torchData)

# Start Exploring : https://pytorch.org/tutorials/
# https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py
##############################
# https://chsasank.github.io/
##############################