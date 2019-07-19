from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import r2_score

# 1. Prepare your data
#    Train our MOdel | Supervised Learning
table =  pd.read_csv("advertising.csv")

# X = table.Radio.values
# Y = table.Sales.values

X = table.TV.values
Y = table.Sales.values

print(X)
print()
print(Y)

# 1D Array
print(X.shape)
print(Y.shape)

# Convert Data into 2D Array
# Doubt ?
X = X.reshape(len(X), 1)
Y = Y.reshape(len(Y), 1)

# 2D Array
print(X.shape)
print(Y.shape)

# We need 2D Array to train our LinearRegression Model from sklearn

# 2nd To create a Model
model = LinearRegression()

# 3rd Fit function is to Train Model with Data and Data should be 2d arrays
#            also optimize our model
model.fit(X, Y)

# 4th Prediction on Original Data so as to get predicted Y i.e. Y1 here
Y1 = model.predict(X)

score = r2_score(Y, Y1)
print("Score for our Model is:", score)

b0 = model.intercept_
b1 = model.coef_

print("Interceptor is:", b0)
print("Slope is:", b1)

# y = b0 + b1.x
# In Semi Finals for WC2019, choose any of batsman in any of team
# Predict his score in the matches which he is going to play !! | espn-cric-info