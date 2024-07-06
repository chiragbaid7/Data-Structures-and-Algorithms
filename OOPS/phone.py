from item import Item
class Phone(Item):
    def __init__(self, name, quantity, price, brokenPhones):
        #with super we will have access to all attributes of parent class
        super().__init__(name, price, quantity)
        self.brokenPhones = brokenPhones
        # print(self.__price) #cannot access private member in derived class.

phone = Phone("samsun", 12, 34, 1)
print(phone)