class employee:
    raise_amount = 1.05
    no_of_employees = 0

    def __init__(self , first , second , salary):
        self.first = first
        self.second = second
        self.salary = salary
        employee.no_of_employees += 1
    
    def full_name(self):
        return '{} {}'.format(self.first , self.second)
    
    def email(self):
        return '{}.{}@company.com'.format(self.first.lower(), self.second.lower())
    
    def apply_raise(self):
        self.salary *= employee.raise_amount
    

emp1 = employee("John", "Doe", 50000)
emp2 = employee("Jane", "Smith", 60000)

print(emp1.full_name())
print(emp1.email())

emp1.apply_raise()

print(emp1.salary)

print(employee.no_of_employees)