import os
import sqlite3

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR,'byte.db')

def seed(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()

        items = [['Lockett','Walker','S0001', 45000,'1'],
        ['Coleman', 'Casey', 'S0002', 70000,'1'],
        ['Kilome', 'Franklyn', 'S0003', 67000,'1'],
        ['Santiago', 'Hecton', 'S0004', 100000,'1'],
        ['Valdez','Framber','S0005', 39000,'2'],
        ['Peacock', 'Brad', 'S0006', 51000,'2'],
        ['Guduan', 'Reymin', 'S0007', 67000,'2'],
        ['Cole', 'Gerrit', 'S0008', 55000,'2']]

        sql = '''INSERT INTO employees(last, first, empID, salary, site)
        VALUES (?,?,?,?,?);'''

        for item in items:
            cursor.execute(sql, (item[0],item[1],item[2],item[3],item[4]))

        items = [['Flushing','NY',11368],
        ['Houston', 'TX', 77002]]

        sql = '''INSERT INTO branches(city, state, zip)
        VALUES (?,?,?);'''

        for item in items:
            cursor.execute(sql,(item[0],item[1],item[2]))