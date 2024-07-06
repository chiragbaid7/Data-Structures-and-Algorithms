import csv
class Item:
    #Global variable shared across all instances
    payRate = 0.8
    all = []
    #Why to hardcode, define predefined attributes during instance creation
    def __init__(self, name, price, quantity):
        #For validation purpose
        assert price >=0, f"Price {price} is not greater than 0"
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculateTotalPrice(self):
        return self.__price*self.quantity
    
    def applyDiscount(self):
        self.__price = self.__price * Item.payRate
    
    def __repr__(self):
        #Access name of the class using instance
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
                price= int(item['price']),
                quantity= item['quantity']
            )

    @staticmethod
    def calcualte(num):
        return num*2
    
    @property
    #Property - read only attribute
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, value):
        if(len(value)>2):
            raise Exception("No greater than 2")
        self.__name = value

