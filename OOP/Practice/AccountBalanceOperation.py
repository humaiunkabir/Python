

from AccountHolder import AccountHolder


class AccountBalanceOperation:
    def __init__(self, empId,operationStatus,amount):

        self.empId = empId
        if(operationStatus==1):
            self.debit = 0
            self.credit = 0
            self.balance = amount
        elif(operationStatus==2):
            self.debit = 0
            self.credit = amount
            self.balance = self.balance + self.credit
        elif(operationStatus==3):
            self.debit = amount
            self.credit = 0
            self.balance = self.balance + self.credit
        else:
            return "Invalid Data."


    def currentBalance(self):
        balance = self.balance
        return balance
        