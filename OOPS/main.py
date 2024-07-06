from item import Item

item1 = Item("ioiTV", 10, 2)

# item1._name = "12" #can be modified
# item1.name = "TF" #cannot modify read only attribute
# print(item1.__name) #Cannot read.
# item1.name = 'BffV'
print(item1.price)
item1.applyDiscount()
print(item1.price)
# item1.price = 12

