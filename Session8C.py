# CLASS ASSIGNMENT

"""
class Product:
    def __init__(self):
        self.obj = 0
        self.obj = self.obj + 1

    def static(self):


    def showNumberOfObjects(self):
        print("Total objects are:{}".format(self.obj))

p1 = Product()
p2 = Product()
p3 = Product()
p4 = p1
p5 = p3

p5.showNumberOfObjects()
"""
class Product:
    Counter = 0
    def __init__(self):
        Product.Counter = Product.Counter + 1

    def showNumberOfObjects(self):
        print("Total objects are:  {}".format(Product.Counter))

p1 = Product()
p2 = Product()
p3 = Product()
p4 = p1
p5 = p3

p5.showNumberOfObjects()