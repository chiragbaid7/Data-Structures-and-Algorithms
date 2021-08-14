class Customer:
    def __init__(self,name) -> None:
        self.name=name 
    def __str__(self) -> str:
        return self.name+"..."
    #static method    
    def print_all(customers):
        for customer in customers:
            print(customer)
    #method overriding 
    def __eq__(self, o: object) -> bool:
        return self.name==o.name
    __repr__=__str__

customers=[Customer("chirag"),Customer("rahul")]
Customer.print_all(customers)
print(customers[0]==customers[1])
print(customers)