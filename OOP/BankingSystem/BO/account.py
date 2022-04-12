from tkinter import E
from typing_extensions import Self


class BankAccount:

    totalUser = 0
    accNumber = 1

    # Constructor 
    def __init__(self, name, email, phone, opebalance, address, pinNumber):
        self.name=name
        self.accNumber = BankAccount.accNumber
        self.email = email
        self.phone = phone
        self.accbalance = opebalance
        self.address = address
        self.pinNumber = pinNumber

        BankAccount.totalUser = 2
        BankAccount.accNumber = BankAccount.accNumber + 1

    
    # Methods Or Function
    def accoutInfo(self):
        print(f'Account Name: {self.name}\t Account Number: {self.accNumber}\t Phone Number: {self.phone}\t Email: {self.email}\t Address: {self.address}\t Account Balance: {self.accbalance}')
    

    def deposit(self):
        amount = int(input('Please Enter Amount For Deposit: '))
        if amount > 0:
            self.accbalance = self.accbalance + amount
            print(f'Transaction Completed. Your Current Balance: {self.accbalance}')
        else:
            print('Your Transaction Amount Is Invalid. Please Enter Valid Amount Again')
    
    def withdrawal(self):
        amount = int(input('Please Enter Amount For Widthdrawl: '))
        if (amount>0) :
            if(amount>self.accbalance):
                print('Please Enter Valid Widthdrawal Amount')
            else:            
                self.accbalance = self.accbalance - amount
                print(f'Transaction Completed. Your Current Balance: {self.accbalance}')
        else:
           print('Your Transaction Amount Is Invalid. Please Enter Valid Amount Again')

    def transfer(self, transferedAccount):
        amount = int(input('Please Enter Amount For Transfer: '))
        if (amount>0) :
            if(amount>self.accbalance):
                print('Please Enter Valid Transfer Amount')
            else:            
                self.accbalance = self.accbalance - amount
                transferedAccount.accbalance = transferedAccount.accbalance + amount
                print(f'Transaction Completed. Your Current Balance: {self.accbalance}')
        else:
           print('Your Transaction Amount Is Invalid. Please Enter Valid Amount Again')


 

user1 = BankAccount(name='Md. Humaiun Kabir',email='hk@gmail.com',phone='01708412345',opebalance=5000,address='Dhaka', pinNumber=55223)
print(user1.accoutInfo())



        