
class BankAccount:
    bankName = "Islamic Bank"

    def __init__(self, name: str, email: str, phone:str, address:str, account_no: int ):
        self.name=name
        self.email=email
        self.phone = phone
        self.address = address
        self.pin = phone[-4:]
        self.balance = 0.0
        self.account_no = account_no
        self.active= True
    
    def validate(self):
        nameValidation = True if len(self.name) > 4 else False
        emailValidation = True if self.email.endswith("@gmail.com") else False
        phoneValidation = True if len(self.phone)==11 else False

        return all([nameValidation,emailValidation,phoneValidation])

    def create_account(self):
        if self.validate():
            return self
        else:
            return False
    
    def close_account(self, pin:str):
        if self.account_no>0 and self.pin == pin:
            self.active= False
            return self            
        else:
            return "No Account Found or Invalid PIN."

    def __repr__(self):
        return f"BankAccount(acc_no={self.account_no}, name={self.name}, phone={self.phone}, balance={self.balance})"
