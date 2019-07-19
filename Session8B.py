# CLASS ASSIGNMENT

class Product:
    def __init__(self):
        self.objects = 1

    def increment(self):
        self.objects = self.objects + 1

    def showCount(self):
        print("Object is {}".format(self.objects))

    def showNumberOfObjects(self):
        print("Total objects are:{}".format(self.objects))

p1 = Product()
p2 = Product()
p3 = Product()
p4 = p1
p5 = p3

p1.increment()
p2.increment()
p3.increment()
p4.increment()
p5.increment()

p1.showCount()
p2.showCount()
p3.showCount()
p4.showCount()
p5.showCount()

print()

p5.showNumberOfObjects()   # Total Product Objects : 3