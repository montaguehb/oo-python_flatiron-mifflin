import unittest
from employee import Employee
from manager import Manager

class EmployeeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.michael = Manager(name="michael", department="sales", age=45)
        self.jane = Manager(name="jane", department="corporate", age=40)
        self.dwight = Employee(name="dwight", salary=54001, manager=self.michael.name)
        self.jim = Employee(name="jim", salary=45000, manager=self.michael.name)
        self.andy = Employee(name="andy", salary=55000, manager=self.jane.name)
        return super().setUp()
    
    def tearDown(self) -> None:
        Employee.all = []
        Manager.all = []
        return super().tearDown()

    def test_employee_has_name(self):
        self.assertTrue(hasattr(self.dwight, "name"))
        self.assertEqual(self.dwight.name, "dwight")
    
    def test_name_is_string(self):
        with self.assertRaises(Exception):
            Employee(name=3, salary=50000, manager=self.michael)
            
    def test_employee_has_salary(self):
        self.assertTrue(hasattr(self.dwight, "salary"))
        self.assertEqual(self.dwight.salary, 54001)
    
    def test_salary_is_num(self):
        with self.assertRaises(Exception):
            Employee(name="dwight", salary="54001", manager=self.michael)
    
    def test_employee_has_manager_name(self):
        self.assertTrue(hasattr(self.dwight, "manager"))
        self.assertEqual(self.dwight.manager, "michael")
    
    def test_has_all(self):
        self.assertCountEqual([self.dwight, self.jim, self.andy], Employee.all)
    
    def test_paid_over(self):
        self.assertCountEqual([self.dwight, self.andy], Employee.paid_over(45000))
    
    def test_find_by_department(self):
        self.assertCountEqual([self.dwight, self.jim], Employee.find_by_department("sales"))
    
    def test_tax_brackets(self):
        self.assertCountEqual([self.dwight, self.andy], self.dwight.tax_bracket())