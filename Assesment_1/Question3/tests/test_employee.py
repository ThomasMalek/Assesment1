from unittest import TestCase
import sqlite3
from app import ORM,Employee
from data import schema,seed
import os

DIR = os.path.dirname(__file__)
DBFILENAME = '_ttest.db'
DBPATH = os.path.join(DIR,DBFILENAME)

Employee.dbpath = DBPATH

class TestAccount(TestCase):

    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)
    
    def tearDown(self):
        os.remove(DBPATH)

    def test_branch(self):
        new_emp = Employee(last='Misilits', first='Dan', empID='S00010', salary=85000, site='2')
        x = new_emp.branch()
        self.assertEqual((2, 'Houston', 'TX', 77002),x)
    