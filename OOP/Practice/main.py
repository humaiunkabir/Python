
from AccountBalanceOperation import AccountBalanceOperation
from AccountHolder import AccountHolder
from DatabaseOperation import DatabaseOperation
from Math import Math
from Resturant import Restaurant


# resturant = Restaurant()

# resturant.name = "Food Village"
# resturant.owner = "Md. Kamal Uddin"

# resturant.details()

# resturant.details_with_address("Dhaka")


# a = int(input("Enter value for X: "))
# b = int(input("Enter value for Y: "))

# objMath = Math(a,b)

# print("Sum = ", objMath.sum())
# print("Sub = ", objMath.sub())
# print("Mul = ", objMath.mul())
# print("Div = ", objMath.div())

objDB = DatabaseOperation("ACCDB.DB")

# print("---------------- Banking System Application --------------------")
# print("-----------------------------------------------------------------")
# objAccountHolder = AccountHolder()

# objAccountHolder.empId = objDB.accountHolderMaxID()+1
# objAccountHolder.name = input("Enter Account Holder Name: ")
# objAccountHolder.fathersName = input("Enter Father's Name: ")
# objAccountHolder.mothersName = input("Enter Mother's Name: ")
# objAccountHolder.mobileNo = input("Enter Mobile No: ")
# objAccountHolder.address = input("Enter Account Holder Address: ")
# objAccountHolder.nid = input("Enter Account Holder NID: ")
# objAccountHolder.homeDistrict = input("Enter Account Holder Home District: ")
# objAccountHolder.pin = objAccountHolder.mobileNo[:-4]


# operationStatus = int(input(
#     "Enter Operation Status. For Opening Type 1, For Deposit Type 2 and For Widthdraw Type 3: "))
# amount = int(input("Enter Amount: "))

# objAccBalanceOperation = AccountBalanceOperation(
#     objAccountHolder.empId, operationStatus, amount)

# print(objAccountHolder.showDetails(), "Balance=",
#       objAccBalanceOperation.currentBalance())


# returnValue = objDB.insertOperation(operationStatus, amount, objAccountHolder)

# if(returnValue > 0):
#     print("Data Inserted Successfully!")
# else:
#     print("Failed Operation!")


objDB.showSqlServerData()