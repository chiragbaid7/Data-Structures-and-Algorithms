class Employee:
    raise_amt=1.5

    def __init__(self,first,last,pay):
        self.first=first 
        self.last=last 
        self.pay=pay 

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

    def __str__(self):
        return self.first+" "+self.last 

class Developer(Employee):
    raise_amt=2

    def __init__(self,first,last,pay,pro_lang):
        #let Employee init method handle first,last,pay
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        self.pro_lang=pro_lang

class Manager(Employee):
    raise_amt=5
    def __init__(self,first,last,pay,employees=None):
        #let Employee init method handle first,last,pay
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        if(employees is None):
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
#redcar.__updateSoftware()  not accesible from object.    

dev_1=Developer('Chirag','Baid',2000,"python")
dev_2=Developer('Rahul','Jain',5000,"C++")
mgr_1=Manager("Vanraj","Doshi",80000,[dev_1,dev_2])
print(dev_2)
print(mgr_1)
