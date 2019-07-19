# NAIVE BAYES -> Works on principles of conditional probability
# Bayes Theorem

# ML Algo : Everything will be Mathematical
# 1. Representation : Storage of Data
# 2. Evaluation : Algorithm to process data
# 3. Optimization : To resolve errors and make algo more stronger

"""
    1. Representation
        ** We need data first **
        Data Source can be any souce : internet i.e. html parsing
                                     : csv files from kaggle etc
        Vehicle
            Bike    :   0
            Car     :   1
           Multiple Attributes can distinguish between Bike and Car
           weight
           engine
           Data for Bikes
           100 kgs      100 cc
           150 kgs      110 cc
           180 kgs      150 cc
           200 kgs      180 cc
           Data for Car
           800 kgs      1000 cc
           1000 kgs     1200 cc
           1200 kgs     1300 cc
           1500 kgs     1500 cc
"""

from sklearn.naive_bayes import GaussianNB

# Create the Dataset | Supervised Learning
FEATURES = [ [100, 100],
         [150, 110],
         [180, 150],
         [200, 180],
         [800, 1000],
         [1000, 1200],
         [1200, 1300],
         [1500, 1500]
       ]

LABELS = [0, 0, 0, 0, 1, 1, 1, 1]

NAMES = ["Bike", "Car"]

# 2. Create Model
model = GaussianNB()

# 3. Train Model
model.fit(FEATURES, LABELS)

sampleInput = [180, 150]

predictedClass = model.predict([sampleInput])

print(">> Predicted Class is:", predictedClass)
print(">> Predicted Class is:", predictedClass[0])
print(">> Predicted Class is:", NAMES[predictedClass[0]])