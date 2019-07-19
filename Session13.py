# VIEW
# tkinter -> BUILT-IN Library to create GUI's
from tkinter import *

# import Session12
# from Session12 import Customer
# from Session12 import DBHelper

from Session12 import *

# cRef = Session12.Customer("John", "+91 99999 88888", "john@example.com")
# cRef.showCustomerDetails()

def onClickAdd():
    print("Button Clicked")
    cRef = Customer(None, None, None)
    cRef.name = entryName.get()
    cRef.phone = entryPhone.get()
    cRef.email = entryEmail.get()
    cRef.showCustomerDetails()

    db = DBHelper()
    db.saveCustomerInDB(cRef)
def onClickUpdate():
    print("Button Clicked")
    cRef = Customer(None, None, None)
    cRef.cid = entryID.get()
    cRef.name = entryName.get()
    cRef.phone = entryPhone.get()
    cRef.email = entryEmail.get()
    cRef.showCustomerDetails()

    db = DBHelper()
    db.updateCustomerInDB(cRef)
def onClickDelete():
    print("Button Clicked")
    cRef = Customer(None, None, None)
    cRef.cid = entryID.get()

    db = DBHelper()
    db.deleteCustomerInDB(cRef.cid)

window = Tk()

# Label -> Is a Text Field
lblTitle = Label(window, text="Customer Details")
# To Add Label in Window
lblTitle.pack()

lblID = Label(window, text="Enter Customer ID")
lblID.pack()

entryID = Entry(window)
entryID.pack()

lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer = Button(window, text="Add Customer", command = onClickAdd)
btnAddCustomer.pack()

btnUpdateCustomer = Button(window, text="Update Customer", command = onClickUpdate)
btnUpdateCustomer.pack()

btnDeleteCustomer = Button(window, text="Delete Customer", command = onClickDelete)
btnDeleteCustomer.pack()

# Keep on Running the program/process
window.mainloop()

"""
    Phase-I
    CRUD Operations with GUI -> Done

    Phase-II
    Loyalty Points : 100 -> 1Point 1Re
    > Shopping Amount should be Entered
    > 2 : 3500 | 10Percent | 350+100 = 450
    > Check Loyalty Points
    > Redeem Loyalty Points
        shopping amount > 500
        in 1 billing only 150 can be redeemed maximum
"""