import sqlite3
from .orm import ORM

class Branch(ORM):
    tablename = 'branches'
    fields = ['city', 'state', 'zip']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.zip = kwargs.get('zip')