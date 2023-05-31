class Employee:
    all = []
    
    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        Employee.all.append(self)
        
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
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int):
            self._salary = salary
        else:
            raise AttributeError

    @property
    def manager(self):
        return self._manager
    
    @manager.setter
    def manager(self, manager):
        if isinstance(manager, str):
            self._manager = manager
        else:
            raise AttributeError
    
    @classmethod
    def paid_over(cls, amount):
        return [employee for employee in cls.all if employee.salary > amount]

    @classmethod
    def find_by_department(cls, department):
        from manager import Manager
        department_managers = [manager.name for manager in Manager.all if manager.department == department]
        return next(employee for employee in cls.all if employee.manager in department_managers)

    def tax_bracket(self):
        return [employee for employee in Employee.all if employee.salary in range(self.salary, self.salary + 1000)]
    
    