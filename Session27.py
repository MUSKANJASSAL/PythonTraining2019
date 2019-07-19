# DECISION TREE
# CART Algo -> Make an Algorithm

# Entropy
# Information Gain

# Iris DataSet
from sklearn.datasets import load_iris
from sklearn import tree

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

# Let's create a Model
model = tree.DecisionTreeClassifier()

# Train the Model -> Supervised Learning
model.fit(irisData.data, irisData.target)

# Let's test our Model
inputData = [5.5, 2.6, 4.4, 1.2]  # -> versicolor type of Iris class

predictedClass = model.predict([inputData])
print()
print(">> Predicted Flower Type is:", predictedClass)
# print(">> Predicted Flower Type is:", predictedClass[0])
# print(">> Predicted Flower Type is:", irisData.target_names[predictedClass[0]])

# Export our Data as Graph Visual !!
import graphviz
data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(data)
graph.render("IRIS DATASET TREE")
graph.view()