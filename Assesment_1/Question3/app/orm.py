import sqlite3

class ORM:
    dbpath = ''
    tablename = ''
    fields = []

    def __init__(self,**kwargs):
        raise NotImplementedError

    def __init__(self, **kwargs):
        """ __init__ must have a self.column = kwargs.get('column') for each
        column in the database table, including the primary key, which must
        be called 'pk'. Raises NotImplementedError by default. """
        raise NotImplementedError

    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            fieldlist = ", ".join(self.fields)
            question_marks = ", ".join(['?' for _ in self.fields])
            SQLPATTERN = """ INSERT INTO {tablename} ({fieldlist})
                                VALUES ({question_marks}) """
            SQL = SQLPATTERN.format(
                tablename=self.tablename,
                fieldlist=fieldlist,
                question_marks=question_marks)
            values = [getattr(self, field) for field in self.fields]
            curs.execute(SQL, values)
            pk = curs.lastrowid
            self.pk = pk

    def _update(self):
        field_eqs = ["{field}=?".format(field=field) for field in self.fields]
        set_tos = ", ".join(field_eqs)
        SQLPATTERN = """ UPDATE {tablename} SET {set_tos}
                            WHERE PK = ? """
        SQL = SQLPATTERN.format(
                tablename=self.tablename, set_tos=set_tos)

        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()

            columnvalues = [getattr(self, field) for field in self.fields]
            values = columnvalues + [self.pk]
            curs.execute(SQL, values)

    def delete(self):
        if self.pk: 
            SQLPATTERN = "DELETE FROM {tablename} WHERE pk=?; "
            SQL = SQLPATTERN.format(tablename=self.tablename)

            with sqlite3.connect(self.dbpath) as conn:
                curs = conn.cursor()
                curs.execute(SQL, (self.pk, ))

        for field in self.fields + ['pk']:
            setattr(self, field, None)
