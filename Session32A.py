from sklearn.cluster import KMeans

# Representation of Data
data = [
              [100, 110],
              [120, 150],
              [150, 200],
              [180, 220],
              [1000, 800],
              [1200, 1200],
              [1500, 1400],
              [2000, 1800]
           ]

# Lets do not keep any labels for our data
# and k means clustering should do the labeling for us
# labels = [0, 0, 0, 0, 1, 1, 1, 1]
clusture = 2

# Model Creation
model = KMeans(n_clusters=clusture)

# Model Training
# We are not mentioning labels :)
model.fit(data)

# predictedClass = model.predict(data)
# print(predictedClass)

sampleInput = [800, 1000]
predictedClass = model.predict([sampleInput])
print(predictedClass)