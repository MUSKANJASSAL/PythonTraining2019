# Explore iris data set with Naive Bayes :)
# Links to Data Sets
# https://data.gov.in/
# https://github.com/jbrownlee/Datasets
# Create account on https://app.chime.aws/
# NAVIE BAYES

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

irisData = load_iris()
print("=====IRIS DATASET=====")
print(irisData)
print()
print("Type:",type(irisData))
print()

# Array of Features
print(irisData.data)
print()

# Array of Targets
print(irisData.target)
print()

# Array of Target Names
print(irisData.target_names)

# 2. Create Model
model = GaussianNB()

# 3. Train Model
model.fit(irisData.data, irisData.target)

# Let's test our Model
inputData = [5.5, 2.6, 4.4, 1.2]  # -> versicolor type of Iris class

predictedClass = model.predict([inputData])

print(">> Predicted Class is:", predictedClass)
# print(">> Predicted Class is:", predictedClass[0])
# print(">> Predicted Class is:", inputData[predictedClass[0]])
