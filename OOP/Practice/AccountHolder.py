
class AccountHolder:

    def __init__(self):
        self._empId = 0
        self._name = ""
        self._fathersName = ""
        self._mothersName = ""
        self._mobileNo = ""
        self._address = ""
        self._nid = ""
        self._homeDistrict = ""
        self._pin = 0

        # using property decorator a getter function
        @property
        def empId(self):
            return self.empId

        # a setter function
        @empId.setter
        def age(self, empId):             
            self._empId = empId 
        
         # using property decorator a getter function
        @property
        def name(self):
            return self.name

        # a setter function
        @name.setter
        def name(self, name):             
            self._name = name 
        
         # using property decorator a getter function
        @property
        def fathersName(self):
            return self.fathersName

        # a setter function
        @fathersName.setter
        def fathersName(self, fathersName):             
            self._fathersName = fathersName 

        # using property decorator a getter function
        @property
        def mothersName(self):
            return self.mothersName

        # a setter function
        @mothersName.setter
        def mothersName(self, mothersName):             
            self._mothersName = mothersName 

        # using property decorator a getter function
        @property
        def mobileNo(self):
            return self.mobileNo

        # a setter function
        @mobileNo.setter
        def mobileNo(self, mobileNo):             
            self._mobileNo = mobileNo 
        
        # using property decorator a getter function
        @property
        def address(self):
            return self.address

        # a setter function
        @address.setter
        def address(self, address):             
            self._address = address 
        
        # using property decorator a getter function
        @property
        def homeDistrict(self):
            return self.homeDistrict

        # a setter function
        @homeDistrict.setter
        def homeDistrict(self, homeDistrict):             
            self._homeDistrict = homeDistrict 

        # using property decorator a getter function
        @property
        def pin(self):
            return self.pin

        # a setter function
        @pin.setter
        def pin(self, pin):             
            self._pin = pin 

        # using property decorator a getter function
        @property
        def nid(self):
            return self.nid

        # a setter function
        @nid.setter
        def nid(self, nid):             
            self._nid = nid 


    def showDetails(self):
        accountHolderInfo = "Name= " + self.name + "\n Fathers Name: " + self.fathersName + "\n Mothers Name: " + self.mothersName + "\n Mobile Name: " + self.mobileNo + "\n Address: " + self.address + "\n NID: " + self.nid + "\n Home District: " + self.homeDistrict 
        return accountHolderInfo
    
    
    