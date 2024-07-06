import csv
class Item:
    #Global variable shared across all instances
    payRate = 0.8
    #Why to hardcode, define predefined attributes during instance creation
    def __init__(self, name, price, quantity):
        #For validation purpose
        assert price >=0, f"Price {price} is not greater than 0"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    
    def calculateTotalPrice(self):
        return self.price*self.quantity
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        #More human readable form
        return f"The item is {self.name} and price is ${self.price}"

    @classmethod
    def instantiateFromCSV(cls):
        with open('items.csv') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item( 
                name = item['name'],
                price = int(item['price']),
                quantity= item['quantity']
            )

    @staticmethod
    def isInteger(num):
        return True if isinstance(num,float) else False


# item = Item("Phone", 10, 5)
# item2 = eval(repr(item)) #Created new object
# print(item2)
# print(str(item))
# Item.instantiateFromCSV()
print(Item.all) #when you want to print objects in console and repr is invoked if it is implemented on each object

#Inheritance
class Phone(Item):
    def __init__(self, name, quantity, price, brokenPhones):
        #with super we will have access to all attributes of parent class
        super().__init__(name, quantity, price)
        self.brokenPhones = brokenPhones

item = Item("Phone", 10, 5)
phone = Phone("samsung", 12, 20, 1)
#Both will print same
print(Phone.all)
print(Item.all)


