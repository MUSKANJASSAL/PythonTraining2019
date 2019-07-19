# SUPERVISED LEARNING
# Based on Labels -> Results

"""
    Linear Regression

    Data is knows to us before hand
    Hence, supervised Learning
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]

    Equation of Line (Regression line)
    Y = b0 + b1X

    Primary Objective is To Find Slope of Line i.e. b1 !!

    Mean of X : MX | 3
                MY | 4

    Step1:
    ----------------------------------------------------------------
    X   Y    X-MX    Y-MY    Sq(X-MX)     (X-MX)(Y-MY)
    ----------------------------------------------------------------
    1   2     -2      -2        4              4
    2   4     -1       0        1              0
    3   5      0       1        0              0
    4   4      1       0        1              0
    5   5      2       1        4              2
    ----------------------------------------------------------------

    Step2:
    Sum of Sq(X-MX)        :  10
    Sum of (X-MX)(Y-MY)    :  6

    b1 is slope of Line
    b1 = [Sum of (X-MX)(Y-MY)] / [Sum of Sq(X-MX)]
    b1 = 6/10
    b1 = 0.6

    Step3:
    Equation of Line
    ================
    Y = b0 + (0.6)X

    Put the mean value of X and Y in equation to find b0
    4 = b0 + (0.6) * 3
    b0 = 2.2

    ======================
    Final Equation of Line
    ======================
    Y = 2.2 + (0.6)X
    ======================

    Step4:
    Calculate  eroors !!
    Check for rrors if they are more or less !!
    If errors are less we are good to go else we have to optimize our data or any other part of program

    1. MSE
    2. R2
    3. Variance

    Lets find MSE
    Substitute original values of X and compute Y with equation of Line

    Y = 2.2 + (0.6)X

    ----------------------------------------------------------------
    X   Y     Y'     Y-MY     Sq(Y-MY)     Y'-MY      Sq(Y'-MY)
    ----------------------------------------------------------------
    1   2    2.8      -2          4        -1.2         1.44
    2   4    3.4       0          0        -0.6         0.36
    3   5     4        1          1          0            0
    4   4    4.6       0          0         0.6         0.36
    5   5    5.2       1          1         1.2         1.44
    ----------------------------------------------------------------

    MSE = [Sum of Sq(Y'-MY)] / [Sum of Sq(Y-MY)]
    MSE = 3.6/6
    MSE = 0.6

    If MSE is 0 it means Regression Line is PERFECT
    MSE should be nearly 0 so as our predictions can go better
"""

import math
import numpy as np

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

arr1 = np.array(X)
print("X:",arr1)
print("=====================")
arr2 = np.array(Y)
print("Y:",arr2)
print("=====================")
MX = arr1.mean()
print("Mean of X is:",MX)
print("=====================")
MY = arr2.mean()
print("Mean of Y is:",MY)
print("=====================")
data1= []
square = []
for X in range(1, 6):
     data1.append(X-MX)
     square.append((X-MX)*(X-MX))
print("(X-MX) is:",data1)
print("=====================")
print("Sq(X-MX) is:",square)
print("=====================")
# print(len(arr2))
print("=====================")
print("(Y-MY) is:",list(Y-MY))
print("=====================")
print("(X-MX)(Y-MY) is:",data1*(Y-MY))
print("=====================")
print("Sum of Sq(X-MX) is:",np.sum(square))
print("=====================")
print("Sum of (X-MX)(Y-MY) is:",np.sum(data1*(Y-MY)))
print("=====================")
b1 = np.sum(data1*(Y-MY)) / np.sum(square)
print("Slope is:",b1)
print("=====================")
print("Equation: Y = b0 + b1X")
print("=====================")
b0 = lambda X,Y,b1: Y - b1*X
print(b0(MX,MY,b1))
print("=====================")
print("Substitute original values of X and compute Y with equation of Line: Y' = 2.2 + (0.6)X")
print("=====================")
print("(Y-MY) is:",list(Y-MY))
print("=====================")
print("Sq(Y-MY) is:",((Y-MY)*(Y-MY)))
s = np.array(((Y-MY)*(Y-MY)))
print("=====================")
A = MY
print(A)
print("=====================")
Y = lambda X: 2.2 + (0.6) * X
data2 = []
for X in range(1, 6):
     data2.append(Y(X))
print("Y' is:",data2)
print("=====================")
print("(Y'-MY) is:",list(data2-A))
print("=====================")
arr = np.array((data2-A))
arr3 = arr*arr
print("Sq(Y'-MY) is:",list(arr3))
print("=====================")
print("Sum of Sq(Y'-MY) is:",np.sum(arr3))
print("=====================")
print("Sum of Sq(Y-MY) is:",np.sum(s))
print("=====================")
MSE = np.sum(arr3) / np.sum(s)
print("MSE is:",MSE)