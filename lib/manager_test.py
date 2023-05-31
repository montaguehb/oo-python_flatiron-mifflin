import unittest
from employee import Employee
from manager import Manager

class ManagerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.michael = Manager(name="michael", department="sales", age=45)
        self.jane = Manager(name="jane", department="corporate", age=40)
        self.dwight = Employee(name="dwight", salary=50000, manager=self.michael.name)
        self.jim = Employee(name="jim", salary=45000, manager=self.michael.name)
        self.andy = Employee(name="andy", salary=55000, manager=self.jane.name)
        return super().setUp()
    
    def tearDown(self) -> None:
        Employee.all = []
        Manager.all = []
        return super().tearDown()
    
    def test_manager_has_name(self):
        self.assertEqual(self.michael.name, "michael")
    
    def test_name_is_string(self):
        with self.assertRaises(Exception):
            Manager(name=45, department="sales", age=45)
    
    def test_manager_has_department(self):
        self.assertEqual(self.michael.department, "sales")
    
    def test_department_is_string(self):
        with self.assertRaises(Exception):
            Manager(name="michael", department=45, age=45)
    
    def test_manager_has_age(self):
        self.assertEqual(self.michael.age, 45)
    
    def test_age_is_num(self):
        with self.assertRaises(Exception):
            Manager(name="michael", department="sales", age="45")
    
    def test_manager_has_all(self):
        self.assertCountEqual([self.michael, self.jane], Manager.all)
    
    def test_hire_employee(self):
        new_employee = self.michael.hire_employee(name="andy", salary=50000)
        self.assertIn(new_employee, Employee.all)
    
    def test_list_all_departments(self):
        self.assertCountEqual(["corporate", "sales"], Manager.all_departments())
    
    def test_average_age(self):
        self.assertEqual(42.5, Manager.average_age())
        self.assertIsInstance(Manager.average_age(), float)
    
    