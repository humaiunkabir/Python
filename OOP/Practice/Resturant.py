

class Restaurant:

    name = ''
    owner = ''

    def details(self):
        print(self.name, self.owner)
    
    def details_with_address(self, address):
        print(self.name, self.owner, address)