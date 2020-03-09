import sqlite3
from .orm import ORM

class Employee(ORM):
    tablename = 'employees'
    fields = ['last', 'first', 'empID', 'salary', 'site']


    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.last = kwargs.get('last')
        self.first = kwargs.get('first')
        self.empID = kwargs.get('empID')
        self.salary = kwargs.get('salary')
        self.site = kwargs.get('site')

    def branch(self):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()

            sql = '''SELECT * FROM branches WHERE pk=?;'''
            values = self.site
            cursor.execute(sql,values)
            row = cursor.fetchone()
            return row

    @classmethod
    def rich_select(cls):
        with sqlite3.connect(cls.dbpath) as connection:
            cursor = connection.cursor()

            sql = '''SELECT * FROM employees WHERE salary>70000;'''

            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
            
    @classmethod
    def salary_update(cls,empID,new_sal):
        with sqlite3.connect(cls.dbpath) as connection:
            cursor = connection.cursor()

            sql = f'''UPDATE employees SET salary=?
            WHERE empID=?;'''

            values = (new_sal,empID)
            cursor.execute(sql,values)