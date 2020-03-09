import os
import sqlite3
from app import Branch, Employee, ORM

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR,'data','byte.db')
ORM.dbpath=DBPATH


# new_emp = Employee(last='Damiano', first='Tommy', empID='S00011', salary=500, site='1')
# Employee.salary_update('S0009',83000)