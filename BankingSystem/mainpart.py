
from BO.BankAccount import BankAccount

bankDatabase = dict()
init_account_no = 10000

print("Banking System.\n")
print("To Create A Bank Account. Please Provide Some Information.\n")


print("1. Create Account\n")
print("2. Close Account\n")
operationItem=0

for looptime in range(100):
    operationItem = int(input("Please Enter Operation Item No 1/2. Or Exit This Program Operation Item No Will Be 3:  "))
    print(operationItem)
    if operationItem == 1:
        name = input("Please Enter Name: ")
        email = input("Please Enter Email: ")
        phone = input("Please Enter Phone No: ")
        address = input("Please Enter Address: ")

        objAccount = BankAccount(name,email,phone,address,init_account_no)

        if objAccount.create_account() == False:
            print("Invalid Data!")
        else:
            bankDatabase[init_account_no]=objAccount
            print(objAccount.validate())
            print("New Account Creation Successfully Completed.")
            print(bankDatabase[init_account_no])
            init_account_no += 1
    elif operationItem==2:
        init_account_no = input("Please Enter Account No: ")
        pin = input("Please Enter PIN: ")
        bankDatabase[init_account_no]
        print (bankDatabase[init_account_no])
        objAccount = BankAccount(bankDatabase[init_account_no].name, bankDatabase[init_account_no].email, bankDatabase[init_account_no].phone, bankDatabase[init_account_no].address, init_account_no)
        objAccount.active = False
        print(objAccount.active)
    elif operationItem==3:
        break



