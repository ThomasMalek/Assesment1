import sqlite3

#Branch = city state zip
#Employee = First Last Empid Salary
#Branch many employee, emp one branch

def schema(dbpath='byte.db'):
    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()

        sql = '''CREATE TABLE branches(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            city VARCHAR(12),
            state VARCHAR(4),
            zip INTEGER
        );'''

        cursor.execute(sql)

        sql = '''CREATE TABLE employees(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            last VARCHAR(24),
            first VARCHAR(24),
            empID VARCHAR(12),
            salary FLOAT,
            site VARCHAR(24),
            FOREIGN KEY(site) REFERENCES branches(pk)
        );'''

        cursor.execute(sql)

# if __name__ == '__main__':
#     schema()