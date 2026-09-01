class Employee:
    def __init__(self,bonus,salary):
        self.bonus=bonus
        self.salary=salary
    def calculatesalary(self):
        print("Base salary calculation for Employee.")


class Manager(Employee):
    def __init__(self,bonus,salary):
        super().__init__(bonus,salary)
    def calculatesalary(self):
        return self.bonus+self.salary

class Developer(Employee):
    def __init__(self,salary,hourswork):
        super().__init__(0,salary)
        self.hourswork=hourswork
    def calculatesalary(self):
        return  self.salary*self.hourswork

salary=float(input("enter salary"))
bonus=float(input("enter bonus"))
hourswork=int(input("enter hours work"))

obj=[Manager(bonus,salary),Developer(salary,hourswork),Employee(bonus,salary)]

for a in obj:
    print(a.calculatesalary())