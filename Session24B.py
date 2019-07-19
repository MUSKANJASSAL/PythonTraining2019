import matplotlib.pyplot as plt
import numpy as np
import math as m
import pandas as pd

table = pd.read_csv("advertising.csv")

#print(table)
#print(table["TV"])
#print(table["Sales"])
X=table["TV"]
Y=table["Sales"]
x=np.array(X)
y=np.array(Y)
mx=x.mean()
#print(mx)
my=y.mean()
sub1=x-mx
sub2=y-my
sq1=sub1**2
mul=sub1*sub2
#print(mul)
sumSq1=sum(sq1)
sumMul=sum(mul)
#print(sumSq1)
#print(sumMul)
b1=sumMul/sumSq1
print(b1)
b=my-b1*mx
print(b)
yd=b + b1*x
#print(yd)
#print(type(x))
#print(type(b1))
sq2=sub2**2
#print(sq2)
sub2d=yd-my
#print(sub2d)
sq2d=sub2d**2
#print(sq2d)
sumSq2=sum(sq2)
#print(sumSq2)
sumSq2d=sum(sq2d)
#print(sumSq2d)
MSE=sumSq2d/sumSq2
print(MSE)
maxX = np.max(X) + 10
minX = np.min(X) - 10
x = np.linspace(minX, maxX, 100)
y = b + b1*x

plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
# plt.plot(X, Y, "o")
plt.plot(x, y, color="r", label="Regression Line")
plt.scatter(X, Y, color="b", label="Data Points")
plt.legend()
plt.show()