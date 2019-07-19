# import Session17E
# import Session17E as ss
# from Session17E import hello, bye
from Session17D import *

# import db.DBHelper
# import db.DBHelper as db
from db import DBHelper


"""
Session17D.hello("John")
Session17D.bye("John")
print(Session17D.companyName)
eRef = Session17D.Employee(101, "Fionna", 30000)
eRef.showEmployee()
"""

"""
ss.hello("John")
ss.bye("John")
print(ss.companyName)
eRef = ss.Employee(101, "Fionna", 30000)
eRef.showEmployee()
"""

# hello("John")
# bye("John")

# db.saveCustomer("john","+919876552512", "john@example.com")
DBHelper.saveCustomer("john","+919876552512", "john@example.com")