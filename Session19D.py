import numpy as np
arr = np.genfromtxt("CityTemps.csv", delimiter=",")
print(arr)
print(arr[0])
print(arr[1])
print(arr[1][0])

temp = open("CityTemps.csv","r")
total = 0
maxt = 0.0
for line in temp:
    try:
        p = float(line.split(",")[1])
        total += 1
        maxt = max(maxt,p)
    except:
        pass
print("Maximum:",maxt)


# Assignment #4 | Part-1
# Data Analysis -> use as much as you can use numpy and its built in functions
# Results
# 1. How many Years
# 2. Find the City with min temperature and in which month
# 3. Find the City with max temperature and in which month
# 4. Add year wise summary
# 5. Sort the Months as per temperature for all three different cities

# Project #2 : From Kaggle download a numeric dataset and analyse it with numpy
