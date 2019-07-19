class mart:
    def __init__(self, name, loct):
        self.name = name
        self.loct = loct

    """def showdetails(self, name, loct):
        print("Name of the Mart is {}".format(name))
        print("Location of the Mart is {}".format(loct))"""

    def showdetails(self):
        print("=================")
        print("Name of the Mart is:\t", self.name)
        print("Location of the Mart is:\t", self.loct)
        print("=================")

class food(mart):
    def foodDetails(self, catg, price, qty, sub_total=0):
        self.catg = catg
        self.price = price
        self.qty = qty
        self.sub_total += self.qty * self.price

    def showfoodDetails(self):
        print("=================")
        print("Category of Food Item:\t", self.catg)
        print("Price of Food Item:\t", self.price)
        print("Quantity of Food Item:\t", self.qty)
        print("Sub Total of Food Section:\t", self.sub_total)
        print("=================")

m = mart("MBD", "Ldh")
m.showdetails()
f = food("pizza", 500, 2)
f.showfoodDetails()