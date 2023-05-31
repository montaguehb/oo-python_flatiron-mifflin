from employee import Employee
class Manager:
    all = []
    
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        Manager.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise AttributeError
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            raise AttributeError

    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, department):
        if isinstance(department, str):
            self._department = department
        else:
            raise AttributeError
        
    def hire_employee(self, name, salary):
        return Employee(name=name, salary=salary, manager=self.name)
    
    @classmethod
    def all_departments(cls):
        return list({manager.department for manager in cls.all})
    
    @classmethod
    def average_age(cls):
        return sum((manager.age for manager in cls.all))/len(cls.all)