class Employee:

    '''
    class varaible can be either globally unique amonge the class. or be a value that act as a default value and later to be 
    overwriiten by instance.
    '''
    nums_of_emps = 0 # this is class variable --> something that should be globally value for the class
    raise_amount = 1.04 # this also a class variable --> but this value should be able to overwritten by instance

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.nums_of_emps +=1

    @property
    def fullname (self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email (self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @fullname.setter
    def fullname (self, name):
        first, last = name.split(' ')
        self.first, self.last = first, last

    @fullname.deleter
    def fullname (self):
        print('Name deleted!')
        self.first, self.last = None, None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    '''
    class method: method related directly with class
    '''
    @classmethod
    def set_raise_amount(cls, amount): #first arg will always be class associate
        cls.raise_amount = amount

    #class method can also act as altenative constructor
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return  cls(first, last, pay) #return an instance by creating a new one

    '''
    static method: method that somewhat has an action on object but no attribute from class/instance require
    '''
    @staticmethod
    def is_workday(day): #all arg can be pass as regular function
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    ''' 
    dunder/magic
    this is special method that was built in for every class
    they can be overloaded
    '''
    # repr: this is intend to be return as class constructor and fallback for str's class
    def __repr__(self):
        return 'Employee("{}","{}","{}")'.format(self.first, self.last, self.pay)

    # str: this method is for showing string to end user
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

class Developer(Employee):
    raise_amount = 1.10 # overwritten a parent attribute

    def __init__(self, first, last, pay, prog_lang):
        # prog_lang: new properties for developer
        super().__init__(first, last, pay) # super(): calling parent class
        self.prog_lang = prog_lang

        # # Alternatively, you can also create construct like below code
        # Employee(self, first, last, pay)

class Manager(Employee):
    
    def __init__(self, first, last, pay, emp = None):
        super().__init__(first, last, pay)
        if emp is None:
            self.empployee = []
        else:
            self.empployee = emp

    def add_emp(self, emp):
        if emp not in self.empployee:
            self.empployee.append(emp)
            print('Employee is added to your org chart')
        else:
            return 'This employee was part of org chart'

    def remove_emp(self, emp):
        if emp in self.empployee:
            self.empployee.remove(emp)
            print('Employee is removed to your org chart')
        else:
            return 'This employee was not part of org chart'

    def print_employee(self):
        for emp in self.empployee:
            print('-->' + emp.fullname())

   
# emp1 = Employee('Kittitut', 'Ganchanapiboon', 2000)
# emp2 = Employee('Test', 'User', 2500)

# #tutorial 1

# # this is the same as next line
# print(emp1.fullname())

# # this is behind the secene of what happening on previous line
# print(Employee.fullname(emp1)) # we call method directly on class and pass the instance 

# # totorial2
# print(Employee.nums_of_emps)

# emp1 = Employee('Kittitut', 'Ganchanapiboon', 2000)
# emp2 = Employee('Test', 'User', 2500)

# print(Employee.nums_of_emps) #this will increment to two
# print('-----------------')
# emp1.raise_amount = 1.05

# print('Class raise amount {}'.format(Employee.raise_amount))
# print('emp1 raise amount {}'.format(emp1.raise_amount))
# print('emo2 raise amount {}'.format(emp2.raise_amount))


# # tutorial 3 
# emp_str1 = 'Jon-Doe-500'
# emp_str2 = 'Marry-Wei-2500'

# emp1 = Employee.from_string(emp_str1)
# emp2 = Employee.from_string(emp_str2)

# print(emp1.fullname())
# print(emp2.fullname())


# import datetime
# my_date = datetime.date(2024,7,3)
# print(Employee.is_workday(my_date))


# # tutorial 4
# dev1 = Developer('Kittitut', 'Ganchanapiboon', 2000,'Python')
# dev2 = Developer('Test', 'User', 2500,'Java')

# # print(dev1.fullname())

# mng1 = Manager('Sue','Xi',90000,[dev1])


# mng1.add_emp(dev2)
# mng1.remove_emp(dev1)
# mng1.print_employee()


# '''
# bonus for tutorial 4
# '''
# print(isinstance(mng1,Employee)) # check if instance(1st arg) is part of inheritance chain on arg2
# print(issubclass(Manager,Employee)) #check if arg1 is subclass of arg2 
# print(help(Developer)) # explain built-in's function for class 

# # tutorial5
# emp1 = Employee('Kittitut', 'Ganchanapiboon', 2000)
# emp2 = Employee('Test', 'User', 2500)

# print(emp1)

# print(emp1.__str__())
# print(emp1.__repr__())

# tutorial6

emp1 = Employee('Kittitut', 'Ganchanapiboon', 2000)
emp2 = Employee('Test', 'User', 2500)

emp1.fullname = 'John Doe'
print(emp1)
print(emp1.fullname)
print(emp1.email)

del emp1.fullname