class Employee():
    
    numemp = 0
    raiseamt = 1.04
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay

        Employee.numemp +=1

    def monthly(self):
        return self.pay//12

    def raisepay(self):
        self.pay = int(self.pay*self.raiseamt)

    def __str__(self):
        return f"Name : {self.name}, pay: {self.pay}"


emp1 = Employee("anurag",700000)
emp2 = Employee("Deore",12000)

emp1.raieamt = 1.06
print(emp1)